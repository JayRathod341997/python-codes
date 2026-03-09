# ============================================================
#  UNION, INTERSECTION, DIFFERENCE — Applied Examples
#  Real-world context: E-learning platform & skill analysis
# ============================================================

# Skills of candidates applying for a job
required_skills = {"Python", "SQL", "Git", "Docker", "Linux"}

candidates = {
    "Alice" : {"Python", "SQL", "Git", "Docker", "Linux", "Kubernetes"},
    "Bob"   : {"Python", "SQL", "JavaScript", "React"},
    "Carol" : {"Python", "Git", "Linux", "Bash", "Docker"},
    "Dave"  : {"Java", "SQL", "Git", "Maven", "Linux"},
    "Eve"   : {"Python", "SQL", "Git", "Docker", "Linux"},
}

print("Required skills:", sorted(required_skills))
print()

# ============================================================
#  INTERSECTION — skills the candidate HAS that are required
# ============================================================

print("=== Matching Skills (Intersection) ===")
for name, skills in candidates.items():
    matched   = required_skills & skills
    missing   = required_skills - skills
    extra     = skills - required_skills
    match_pct = len(matched) / len(required_skills) * 100
    print(f"  {name:<6}: matched={sorted(matched)}  missing={sorted(missing)}  "
          f"fit={match_pct:.0f}%")

# ============================================================
#  Full match — candidate has ALL required skills
# ============================================================

print("\n=== Perfect Fit Candidates ===")
for name, skills in candidates.items():
    if required_skills.issubset(skills):   # all required ⊆ their skills
        extra = skills - required_skills
        print(f"  {name} QUALIFIES  (bonus skills: {extra})")

# ============================================================
#  UNION — all skills available across ALL candidates
# ============================================================

print("\n=== Skill Pool (All Candidates Combined) ===")
all_skills = set()
for skills in candidates.values():
    all_skills |= skills    # union-update in-place

print("All available skills:", sorted(all_skills))
print("Total unique skills :", len(all_skills))

# ============================================================
#  DIFFERENCE — skills not covered by any candidate
# ============================================================

print("\n=== Skills Gap (Not covered by anyone) ===")
uncovered = required_skills - all_skills
print("Uncovered skills:", uncovered if uncovered else "None — all skills are covered!")

# Skills required but only ONE candidate has
print("\nRare required skills (only 1 candidate has):")
for skill in required_skills:
    who_has = [name for name, s in candidates.items() if skill in s]
    if len(who_has) == 1:
        print(f"  {skill:<15} → only {who_has[0]}")

# ============================================================
#  Multi-platform user analytics
# ============================================================

print("\n=== Platform Analytics ===")

web_users    = {"U001","U002","U003","U004","U005","U006"}
mobile_users = {"U002","U003","U005","U007","U008"}
tablet_users = {"U001","U003","U009"}

# Users on ALL platforms
all_platforms = web_users & mobile_users & tablet_users
print("Uses all 3 platforms    :", all_platforms)

# Users on web only
web_only = web_users - mobile_users - tablet_users
print("Web only                :", web_only)

# Mobile only
mobile_only = mobile_users - web_users - tablet_users
print("Mobile only             :", mobile_only)

# At least 2 platforms (intersections)
web_and_mobile  = web_users & mobile_users
web_and_tablet  = web_users & tablet_users
mob_and_tablet  = mobile_users & tablet_users
multi_platform  = web_and_mobile | web_and_tablet | mob_and_tablet
print("Multi-platform users    :", multi_platform)

# Total unique users
total_users = web_users | mobile_users | tablet_users
print("Total unique users      :", len(total_users))

# ============================================================
#  Practical: comparing two product categories
# ============================================================

print("\n=== Product Tag Comparison ===")

sports_tags   = {"fitness", "outdoor", "health", "equipment", "running"}
wellness_tags = {"health", "meditation", "fitness", "mental", "nutrition"}

overlap      = sports_tags & wellness_tags
sports_only  = sports_tags - wellness_tags
wellness_only= wellness_tags - sports_tags
combined     = sports_tags | wellness_tags

print("Overlap (cross-sell opportunity):", overlap)
print("Sports-only tags               :", sports_only)
print("Wellness-only tags             :", wellness_only)
print("Combined tags                  :", combined)
