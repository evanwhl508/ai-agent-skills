import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "..");

function readJson(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(repoRoot, relativePath), "utf8"));
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function assertFile(relativePath) {
  assert(fs.existsSync(path.join(repoRoot, relativePath)), `Missing file: ${relativePath}`);
}

function parseFrontmatter(markdown) {
  const match = markdown.match(/^---\n([\s\S]*?)\n---/);
  assert(match, "SKILL.md is missing YAML frontmatter");
  const fields = {};
  for (const line of match[1].split("\n")) {
    const [key, ...rest] = line.split(":");
    fields[key.trim()] = rest.join(":").trim();
  }
  return fields;
}

const skillsManifest = readJson("manifests/skills.json");
const adaptersManifest = readJson("manifests/adapters.json");

assert(skillsManifest.schemaVersion === 1, "skills.json schemaVersion must be 1");
assert(Array.isArray(skillsManifest.skills), "skills.json must contain a skills array");
assert(adaptersManifest.schemaVersion === 1, "adapters.json schemaVersion must be 1");

for (const target of ["codex", "claude-code", "generic"]) {
  assert(adaptersManifest.targets[target], `Missing adapter target: ${target}`);
}

for (const skill of skillsManifest.skills) {
  assert(skill.name, "Skill is missing name");
  assert(skill.path, `${skill.name} is missing path`);
  assert(Array.isArray(skill.targets), `${skill.name} is missing targets`);

  const skillPath = path.join(skill.path, "SKILL.md");
  assertFile(skillPath);

  const skillMarkdown = fs.readFileSync(path.join(repoRoot, skillPath), "utf8");
  const frontmatter = parseFrontmatter(skillMarkdown);
  assert(frontmatter.name === skill.name, `${skill.name} frontmatter name mismatch`);
  assert(frontmatter.description && frontmatter.description.length > 80, `${skill.name} description is too short`);

  for (const reference of skill.references || []) {
    assertFile(reference);
  }
}

assertFile(".codex-plugin/plugin.json");
assertFile(".claude-plugin/plugin.json");
assertFile("bin/ai-agent-skills.js");

console.log(`Validated ${skillsManifest.skills.length} skill(s).`);
