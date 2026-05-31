-- ============================================================
-- 历史平行线 (History Parallel) — Supabase Schema Migration
-- Generated: 2026-05-31
-- ============================================================

-- Enable required extensions
create extension if not exists "uuid-ossp";

-- ============================================================
-- 1. regions — 地区/文明
-- ============================================================
create table if not exists public.regions (
  id          uuid        primary key default uuid_generate_v4(),
  slug        text        not null unique,
  name_zh     text        not null,
  name_en     text        not null,
  parent_id   uuid        references public.regions(id) on delete set null,
  description_zh text,
  description_en text,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

alter table public.regions enable row level security;

-- Public read, admin write
create policy "regions: public read"
  on public.regions for select
  using (true);

create policy "regions: admin insert"
  on public.regions for insert
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "regions: admin update"
  on public.regions for update
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "regions: admin delete"
  on public.regions for delete
  using (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_regions_slug on public.regions(slug);
create index if not exists idx_regions_parent on public.regions(parent_id);

-- ============================================================
-- 2. persons — 历史人物
-- ============================================================
create table if not exists public.persons (
  id            uuid        primary key default uuid_generate_v4(),
  slug          text        not null unique,
  name_zh       text        not null,
  name_en       text        not null,
  alternative_names_zh text[],
  alternative_names_en text[],
  birth_year    integer     not null,
  death_year    integer,
  region_id     uuid        not null references public.regions(id) on delete restrict,
  tags          text[]      default '{}',
  summary_zh    text,
  summary_en    text,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now()
);

alter table public.persons enable row level security;

create policy "persons: public read"
  on public.persons for select
  using (true);

create policy "persons: admin insert"
  on public.persons for insert
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "persons: admin update"
  on public.persons for update
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "persons: admin delete"
  on public.persons for delete
  using (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_persons_slug on public.persons(slug);
create index if not exists idx_persons_region on public.persons(region_id);
create index if not exists idx_persons_birth on public.persons(birth_year);
create index if not exists idx_persons_search on public.persons using gin(to_tsvector('simple', name_zh || ' ' || name_en));

-- ============================================================
-- 3. historical_events — 历史事件
-- ============================================================
create table if not exists public.historical_events (
  id               uuid        primary key default uuid_generate_v4(),
  slug             text        not null unique,
  title_zh         text        not null,
  title_en         text        not null,
  start_year       integer     not null,
  end_year         integer,
  approximate_date_zh text,
  approximate_date_en text,
  region_id        uuid        not null references public.regions(id) on delete restrict,
  place_name_zh   text,
  place_name_en    text,
  tags             text[]      default '{}',
  importance       integer     not null check (importance between 1 and 5),
  summary_zh       text,
  summary_en       text,
  description_zh   text,
  description_en   text,
  related_event_ids uuid[],
  created_at       timestamptz not null default now(),
  updated_at       timestamptz not null default now()
);

alter table public.historical_events enable row level security;

create policy "events: public read"
  on public.historical_events for select
  using (true);

create policy "events: admin insert"
  on public.historical_events for insert
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "events: admin update"
  on public.historical_events for update
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "events: admin delete"
  on public.historical_events for delete
  using (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_events_slug on public.historical_events(slug);
create index if not exists idx_events_region on public.historical_events(region_id);
create index if not exists idx_events_start_year on public.historical_events(start_year);
create index if not exists idx_events_end_year on public.historical_events(end_year);
create index if not exists idx_events_importance on public.historical_events(importance);
create index if not exists idx_events_search on public.historical_events using gin(to_tsvector('simple', title_zh || ' ' || title_en || ' ' || coalesce(summary_zh,'') || ' ' || coalesce(summary_en,'')));

-- ============================================================
-- 4. sources — 史料来源
-- ============================================================
create table if not exists public.sources (
  id          uuid        primary key default uuid_generate_v4(),
  title_zh    text        not null,
  title_en    text        not null,
  author      text,
  url         text,
  publisher   text,
  year        integer,
  note_zh     text,
  note_en     text,
  license     text        default 'CC BY-SA 4.0',
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

alter table public.sources enable row level security;

create policy "sources: public read"
  on public.sources for select
  using (true);

create policy "sources: admin insert"
  on public.sources for insert
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "sources: admin update"
  on public.sources for update
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create policy "sources: admin delete"
  on public.sources for delete
  using (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_sources_title on public.sources(title_zh, title_en);

-- ============================================================
-- 5. tags — 标签字典（可选，用于规范化标签）
-- ============================================================
create table if not exists public.tags (
  id          uuid        primary key default uuid_generate_v4(),
  slug        text        not null unique,
  name_zh     text        not null,
  name_en     text        not null,
  category    text, -- 'person' | 'event' | 'region' | null (both)
  created_at  timestamptz not null default now()
);

alter table public.tags enable row level security;

create policy "tags: public read"
  on public.tags for select
  using (true);

create policy "tags: admin manage"
  on public.tags for all
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_tags_slug on public.tags(slug);
create index if not exists idx_tags_category on public.tags(category);

-- ============================================================
-- 6. event_persons — 事件 ↔ 人物 多对多
-- ============================================================
create table if not exists public.event_persons (
  event_id  uuid  not null references public.historical_events(id) on delete cascade,
  person_id uuid  not null references public.persons(id) on delete cascade,
  primary key (event_id, person_id)
);

alter table public.event_persons enable row level security;

create policy "event_persons: public read"
  on public.event_persons for select
  using (true);

create policy "event_persons: admin manage"
  on public.event_persons for all
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_ep_event on public.event_persons(event_id);
create index if not exists idx_ep_person on public.event_persons(person_id);

-- ============================================================
-- 7. event_sources — 事件 ↔ 来源 多对多
-- ============================================================
create table if not exists public.event_sources (
  event_id  uuid  not null references public.historical_events(id) on delete cascade,
  source_id uuid  not null references public.sources(id) on delete cascade,
  primary key (event_id, source_id)
);

alter table public.event_sources enable row level security;

create policy "event_sources: public read"
  on public.event_sources for select
  using (true);

create policy "event_sources: admin manage"
  on public.event_sources for all
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_es_event on public.event_sources(event_id);
create index if not exists idx_es_source on public.event_sources(source_id);

-- ============================================================
-- 8. event_tags — 事件 ↔ 标签 多对多
-- ============================================================
create table if not exists public.event_tags (
  event_id uuid  not null references public.historical_events(id) on delete cascade,
  tag_id   uuid  not null references public.tags(id) on delete cascade,
  primary key (event_id, tag_id)
);

alter table public.event_tags enable row level security;

create policy "event_tags: public read"
  on public.event_tags for select
  using (true);

create policy "event_tags: admin manage"
  on public.event_tags for all
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_et_event on public.event_tags(event_id);
create index if not exists idx_et_tag on public.event_tags(tag_id);

-- ============================================================
-- 9. person_tags — 人物 ↔ 标签 多对多
-- ============================================================
create table if not exists public.person_tags (
  person_id uuid  not null references public.persons(id) on delete cascade,
  tag_id    uuid  not null references public.tags(id) on delete cascade,
  primary key (person_id, tag_id)
);

alter table public.person_tags enable row level security;

create policy "person_tags: public read"
  on public.person_tags for select
  using (true);

create policy "person_tags: admin manage"
  on public.person_tags for all
  using (auth.jwt() ->> 'role' = 'admin')
  with check (auth.jwt() ->> 'role' = 'admin');

create index if not exists idx_pt_person on public.person_tags(person_id);
create index if not exists idx_pt_tag on public.person_tags(tag_id);

-- ============================================================
-- 10. user_bookmarks — 用户收藏
-- ============================================================
create table if not exists public.user_bookmarks (
  id        uuid        primary key default uuid_generate_v4(),
  user_id   uuid        not null references auth.users(id) on delete cascade,
  event_id  uuid        not null references public.historical_events(id) on delete cascade,
  note_zh   text,
  note_en   text,
  created_at timestamptz not null default now(),
  unique(user_id, event_id)
);

alter table public.user_bookmarks enable row level security;

create policy "bookmarks: owner read"
  on public.user_bookmarks for select
  using (auth.uid() = user_id);

create policy "bookmarks: owner insert"
  on public.user_bookmarks for insert
  with check (auth.uid() = user_id);

create policy "bookmarks: owner update"
  on public.user_bookmarks for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

create policy "bookmarks: owner delete"
  on public.user_bookmarks for delete
  using (auth.uid() = user_id);

create index if not exists idx_bookmarks_user on public.user_bookmarks(user_id);
create index if not exists idx_bookmarks_event on public.user_bookmarks(event_id);

-- ============================================================
-- 11. user_notes — 用户私人笔记
-- ============================================================
create table if not exists public.user_notes (
  id        uuid        primary key default uuid_generate_v4(),
  user_id   uuid        not null references auth.users(id) on delete cascade,
  event_id  uuid        references public.historical_events(id) on delete cascade,
  person_id uuid        references public.persons(id) on delete cascade,
  note_zh   text,
  note_en   text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check (event_id is not null or person_id is not null)
);

alter table public.user_notes enable row level security;

create policy "notes: owner read"
  on public.user_notes for select
  using (auth.uid() = user_id);

create policy "notes: owner insert"
  on public.user_notes for insert
  with check (auth.uid() = user_id);

create policy "notes: owner update"
  on public.user_notes for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

create policy "notes: owner delete"
  on public.user_notes for delete
  using (auth.uid() = user_id);

create index if not exists idx_notes_user on public.user_notes(user_id);
create index if not exists idx_notes_event on public.user_notes(event_id);
create index if not exists idx_notes_person on public.user_notes(person_id);

-- ============================================================
-- updated_at 触发器（所有带 updated_at 的表）
-- ============================================================
create or replace function public.handle_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql security definer;

create or replace trigger trg_regions_updated_at
  before update on public.regions
  for each row execute function public.handle_updated_at();

create or replace trigger trg_persons_updated_at
  before update on public.persons
  for each row execute function public.handle_updated_at();

create or replace trigger trg_events_updated_at
  before update on public.historical_events
  for each row execute function public.handle_updated_at();

create or replace trigger trg_sources_updated_at
  before update on public.sources
  for each row execute function public.handle_updated_at();

create or replace trigger trg_user_notes_updated_at
  before update on public.user_notes
  for each row execute function public.handle_updated_at();

-- ============================================================
-- 种子数据：基础地区（供 mock 数据对应）
-- ============================================================
-- 在 Supabase Dashboard 的 SQL Editor 中手动运行，或通过 migration 插入
-- 这里仅提供 INSERT 模板，实际数据通过 admin UI 或脚本导入

-- insert into public.regions (slug, name_zh, name_en, parent_id, description_zh, description_en) values
--   ('china',      '中国',     'China',     null, '中原王朝及主要政权', 'Major dynasties and polities of China'),
--   ('europe',     '欧洲',     'Europe',    null, '中世纪至近代早期欧洲', 'Medieval to early modern Europe'),
--   ('byzantine',  '拜占庭',   'Byzantine', null, '拜占庭帝国（东罗马帝国）', 'Byzantine Empire (Eastern Roman Empire)'),
--   ('islamic',    '伊斯兰世界', 'Islamic',   null, '中东及北非伊斯兰政权', 'Islamic polities in Mideast and North Africa'),
--   ('japan',      '日本',     'Japan',     null, '日本列岛各历史时期', 'Japanese archipelago across historical periods'),
--   ('india',      '印度',     'India',     null, '南亚次大陆各政权', 'South Asian polities on the Indian subcontinent'),
--   ('song-china', '北宋', 'Northern Song', (select id from public.regions where slug='china'), '北宋王朝（960–1127）', 'Northern Song dynasty (960–1127)'),
--   ('england',    '英格兰', 'England',  (select id from public.regions where slug='europe'), '诺曼征服后的英格兰', 'England after the Norman Conquest')
-- on conflict do nothing;

-- ============================================================
-- 完毕
-- ============================================================
