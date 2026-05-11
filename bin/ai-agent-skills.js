#!/usr/bin/env node

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "..");
const skillsManifestPath = path.join(repoRoot, "manifests", "skills.json");
const adaptersManifestPath = path.join(repoRoot, "manifests", "adapters.json");

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function usage(exitCode = 0) {
  const text = `
Usage:
  ai-agent-skills list
  ai-agent-skills add <skill-name|all> [--target codex|claude-code|generic] [--dir <path>] [--force] [--dry-run]

Examples:
  node bin/ai-agent-skills.js list
  node bin/ai-agent-skills.js add prompt-harness-architect
  node bin/ai-agent-skills.js add all --target codex
  node bin/ai-agent-skills.js add prompt-harness-architect --target claude-code --force
`;
  console.log(text.trim());
  process.exit(exitCode);
}

function parseArgs(argv) {
  const [command, subject, ...rest] = argv;
  const options = {
    command,
    subject,
    target: "codex",
    dir: null,
    force: false,
    dryRun: false
  };

  for (let i = 0; i < rest.length; i += 1) {
    const arg = rest[i];
    if (arg === "--target") {
      options.target = rest[++i];
    } else if (arg === "--dir") {
      options.dir = rest[++i];
    } else if (arg === "--force") {
      options.force = true;
    } else if (arg === "--dry-run") {
      options.dryRun = true;
    } else if (arg === "--help" || arg === "-h") {
      usage(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return options;
}

function defaultInstallDir(target) {
  if (target === "codex") {
    const base = process.env.CODEX_HOME || path.join(os.homedir(), ".codex");
    return path.join(base, "skills");
  }

  if (target === "claude-code") {
    const base = process.env.CLAUDE_HOME || path.join(os.homedir(), ".claude");
    return path.join(base, "skills");
  }

  if (target === "generic") {
    return path.resolve(process.cwd(), "skills");
  }

  throw new Error(`Unsupported target: ${target}`);
}

function copyRecursive(src, dest, { force, dryRun, filter }) {
  if (!fs.existsSync(src)) {
    throw new Error(`Source does not exist: ${src}`);
  }

  if (fs.existsSync(dest)) {
    if (!force) {
      throw new Error(`Destination exists: ${dest}. Re-run with --force to replace it.`);
    }
    if (!dryRun) {
      fs.rmSync(dest, { recursive: true, force: true });
    }
  }

  if (dryRun) {
    console.log(`[dry-run] copy ${src} -> ${dest}`);
    return;
  }

  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.cpSync(src, dest, {
    recursive: true,
    filter
  });
}

function skillFilterForTarget(sourceRoot, adapterConfig) {
  const excludes = adapterConfig.excludePaths || [];
  return (src) => {
    const relative = path.relative(sourceRoot, src).split(path.sep).join("/");
    if (!relative) {
      return true;
    }

    return !excludes.some((excludePath) => (
      relative === excludePath || relative.startsWith(`${excludePath}/`)
    ));
  };
}

function listSkills(manifest) {
  for (const skill of manifest.skills) {
    const status = skill.installable ? "installable" : "not installable";
    console.log(`${skill.name} - ${status} - ${skill.description}`);
  }
}

function resolveSkills(manifest, subject) {
  const installable = manifest.skills.filter((skill) => skill.installable);
  if (subject === "all") {
    return installable;
  }

  const skill = installable.find((item) => item.name === subject);
  if (!skill) {
    throw new Error(`Unknown installable skill: ${subject}`);
  }
  return [skill];
}

function installSkill(skill, options, adaptersManifest) {
  if (!skill.targets.includes(options.target)) {
    throw new Error(`${skill.name} does not support target '${options.target}'.`);
  }

  const adapterConfig = adaptersManifest.targets[options.target];
  if (!adapterConfig) {
    throw new Error(`Missing adapter configuration for target '${options.target}'.`);
  }

  const installRoot = path.resolve(options.dir || defaultInstallDir(options.target));
  const source = path.join(repoRoot, skill.path);
  const destination = path.join(installRoot, skill.name);

  copyRecursive(source, destination, {
    force: options.force,
    dryRun: options.dryRun,
    filter: skillFilterForTarget(source, adapterConfig)
  });

  console.log(`${options.dryRun ? "[dry-run] " : ""}Installed ${skill.name} -> ${destination}`);
}

function main() {
  const argv = process.argv.slice(2);
  if (argv.length === 0 || argv[0] === "--help" || argv[0] === "-h") {
    usage(0);
  }

  const options = parseArgs(argv);
  const manifest = readJson(skillsManifestPath);
  const adaptersManifest = readJson(adaptersManifestPath);

  if (options.command === "list") {
    listSkills(manifest);
    return;
  }

  if (options.command === "add") {
    if (!options.subject) {
      throw new Error("Missing skill name. Use 'all' to install every installable skill.");
    }

    const skills = resolveSkills(manifest, options.subject);
    for (const skill of skills) {
      installSkill(skill, options, adaptersManifest);
    }
    return;
  }

  usage(1);
}

try {
  main();
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
