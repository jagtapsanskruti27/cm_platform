# Graph Report - cm_platform  (2026-07-10)

## Corpus Check
- 79 files · ~35,303 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 247 nodes · 250 edges · 54 communities (29 shown, 25 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `14038b86`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_views.py|views.py]]
- [[_COMMUNITY_GeneralChatConsumer|GeneralChatConsumer]]
- [[_COMMUNITY_models.py|models.py]]
- [[_COMMUNITY_views.py|views.py]]
- [[_COMMUNITY_views.py|views.py]]
- [[_COMMUNITY_What You Must Do When Invoked|What You Must Do When Invoked]]
- [[_COMMUNITY_graphify|/graphify]]
- [[_COMMUNITY_graphify reference extra exports and benchmark|graphify reference: extra exports and benchmark]]
- [[_COMMUNITY_AppConfig|AppConfig]]
- [[_COMMUNITY_graphify reference query, path, explain|graphify reference: query, path, explain]]
- [[_COMMUNITY_graphify reference add a URL and watch a folder|graphify reference: add a URL and watch a folder]]
- [[_COMMUNITY_graphify reference commit hook and native CLAUDE.md integration|graphify reference: commit hook and native CLAUDE.md integration]]
- [[_COMMUNITY_graphify reference incremental update and cluster-only|graphify reference: incremental update and cluster-only]]
- [[_COMMUNITY_graphify reference GitHub clone and cross-repo merge|graphify reference: GitHub clone and cross-repo merge]]
- [[_COMMUNITY_graphify reference transcribe video and audio|graphify reference: transcribe video and audio]]
- [[_COMMUNITY_main|main]]
- [[_COMMUNITY_0001_initial.py|0001_initial.py]]
- [[_COMMUNITY_graphify|graphify.md]]
- [[_COMMUNITY_extraction-spec|extraction-spec.md]]
- [[_COMMUNITY_graphify|graphify.md]]
- [[_COMMUNITY_0001_initial.py|0001_initial.py]]
- [[_COMMUNITY_0002_remove_post_image_post_likes_alter_comment_post.py|0002_remove_post_image_post_likes_alter_comment_post.py]]
- [[_COMMUNITY_0003_post_image.py|0003_post_image.py]]
- [[_COMMUNITY_0004_remove_like_post_remove_like_user_remove_post_likes_and_more.py|0004_remove_like_post_remove_like_user_remove_post_likes_and_more.py]]
- [[_COMMUNITY_0005_userprofile_profile_picture.py|0005_userprofile_profile_picture.py]]
- [[_COMMUNITY_0006_rename_userprofile_profile.py|0006_rename_userprofile_profile.py]]
- [[_COMMUNITY_0007_follow.py|0007_follow.py]]
- [[_COMMUNITY_0008_badge_profile_about_profile_cover_photo_and_more.py|0008_badge_profile_about_profile_cover_photo_and_more.py]]
- [[_COMMUNITY_0009_remove_badge_description_remove_badge_name_and_more.py|0009_remove_badge_description_remove_badge_name_and_more.py]]
- [[_COMMUNITY_0001_initial.py|0001_initial.py]]
- [[_COMMUNITY_settings.py|settings.py]]
- [[_COMMUNITY_wsgi.py|wsgi.py]]
- [[_COMMUNITY_0001_initial.py|0001_initial.py]]
- [[_COMMUNITY_0002_notification_event.py|0002_notification_event.py]]
- [[_COMMUNITY_0003_remove_event_event_date_remove_event_location_and_more.py|0003_remove_event_event_date_remove_event_location_and_more.py]]
- [[_COMMUNITY_0001_initial.py|0001_initial.py]]
- [[_COMMUNITY_0002_follow.py|0002_follow.py]]
- [[_COMMUNITY_0003_notification.py|0003_notification.py]]

## God Nodes (most connected - your core abstractions)
1. `What You Must Do When Invoked` - 12 edges
2. `Event` - 10 edges
3. `/graphify` - 10 edges
4. `GeneralChatConsumer` - 9 edges
5. `PrivateChatConsumer` - 9 edges
6. `Post` - 8 edges
7. `graphify reference: extra exports and benchmark` - 8 edges
8. `AppConfig` - 7 edges
9. `Profile` - 7 edges
10. `Notification` - 6 edges

## Surprising Connections (you probably didn't know these)
- `report_post()` --indirect_call--> `Post`  [INFERRED]
  advanced/views.py → post/models.py
- `ChatConfig` --uses--> `AppConfig`  [INFERRED]
  chat/apps.py → app/apps.py
- `EventConfig` --uses--> `AppConfig`  [INFERRED]
  event/apps.py → app/apps.py
- `PostConfig` --uses--> `AppConfig`  [INFERRED]
  post/apps.py → app/apps.py
- `read_notification()` --indirect_call--> `Notification`  [INFERRED]
  post/views.py → event/models.py

## Import Cycles
- None detected.

## Communities (54 total, 25 thin omitted)

### Community 0 - "views.py"
Cohesion: 0.10
Nodes (9): Block, Report, report_post(), Comment, Follow, Like, Meta, Notification (+1 more)

### Community 1 - "GeneralChatConsumer"
Cohesion: 0.10
Nodes (5): AsyncWebsocketConsumer, GeneralChatConsumer, PrivateChatConsumer, Message, UserStatus

### Community 2 - "models.py"
Cohesion: 0.15
Nodes (13): EventForm, Meta, Event, EventCheckIn, EventGallery, EventJoin, EventMessage, Meta (+5 more)

### Community 3 - "views.py"
Cohesion: 0.11
Nodes (4): Badge, Follow, Meta, UserBadge

### Community 4 - "views.py"
Cohesion: 0.12
Nodes (6): Meta, ProfileForm, Profile, edit_profile(), home(), URL configuration for cm_platform project.  The `urlpatterns` list routes URLs

### Community 5 - "What You Must Do When Invoked"
Cohesion: 0.13
Nodes (15): Part A - Structural extraction for code files, Part B - Semantic extraction (parallel subagents), Part C - Merge AST + semantic into final extraction, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths), Step 1 - Ensure graphify is installed, Step 2.5 - Video and audio (only if video files detected), Step 2 - Detect files, Step 3 - Extract entities and relationships (+7 more)

### Community 6 - "/graphify"
Cohesion: 0.20
Nodes (9): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Usage (+1 more)

### Community 7 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 8 - "AppConfig"
Cohesion: 0.25
Nodes (4): AppConfig, ChatConfig, EventConfig, PostConfig

### Community 9 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 10 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 11 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 12 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

## Knowledge Gaps
- **67 isolated node(s):** `Migration`, `Migration`, `Migration`, `Migration`, `Migration` (+62 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Post` connect `views.py` to `views.py`, `views.py`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Why does `Event` connect `models.py` to `views.py`, `views.py`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Why does `Notification` connect `models.py` to `views.py`, `views.py`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Event` (e.g. with `EventForm` and `Meta`) actually correct?**
  _`Event` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Migration`, `Migration`, `Migration` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09788359788359788 - nodes in this community are weakly interconnected._
- **Should `GeneralChatConsumer` be split into smaller, more focused modules?**
  _Cohesion score 0.09971509971509972 - nodes in this community are weakly interconnected._