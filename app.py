from __future__ import annotations

from datetime import datetime
from html import escape
from typing import Any

import streamlit as st

from curriculum import (
    LESSONS,
    RUBRIC,
    all_questions,
    build_progress_csv,
    build_teacher_guide,
    build_worksheet,
    get_lesson,
    score_answers,
)


st.set_page_config(
    page_title="がんばる日本語ラボ",
    layout="wide",
    initial_sidebar_state="expanded",
)


CSS = """
<style>
:root {
  --ink: #16202a;
  --muted: #5c6b78;
  --line: #d9e2ea;
  --paper: #fbfcfd;
  --soft: #eef6f1;
  --accent: #0f766e;
  --accent-2: #b45309;
  --accent-3: #2563eb;
}
.stApp {
  background: linear-gradient(180deg, #f7faf9 0%, #ffffff 42%);
  color: var(--ink);
}
[data-testid="stSidebar"] {
  background: #f3f7f5;
  border-right: 1px solid var(--line);
}
h1, h2, h3 {
  letter-spacing: 0;
}
.hero {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 22px 24px;
  background: #ffffff;
  box-shadow: 0 10px 30px rgba(22, 32, 42, 0.06);
}
.hero-title {
  font-size: 2.1rem;
  line-height: 1.18;
  font-weight: 800;
  margin-bottom: 8px;
}
.hero-copy {
  color: var(--muted);
  font-size: 1.02rem;
  line-height: 1.7;
  max-width: 860px;
}
.card {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px 18px;
  background: #ffffff;
  min-height: 128px;
}
.card h3 {
  font-size: 1.05rem;
  margin: 0 0 8px 0;
}
.card p, .card li, .card-body {
  color: var(--muted);
  line-height: 1.65;
}
.card-body p {
  margin: 8px 0 0 0;
}
.tag {
  display: inline-block;
  border-radius: 999px;
  padding: 3px 10px;
  background: var(--soft);
  color: var(--accent);
  font-size: 0.82rem;
  font-weight: 700;
  margin-right: 6px;
}
.example {
  border-left: 4px solid var(--accent);
  background: #f8fbfa;
  padding: 12px 14px;
  border-radius: 0 8px 8px 0;
  margin: 8px 0;
}
.example strong {
  color: var(--accent);
}
.small-note {
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.65;
}
.rubric {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px 16px;
  background: #fffdf7;
}
.correct {
  color: #047857;
  font-weight: 700;
}
.incorrect {
  color: #b91c1c;
  font-weight: 700;
}
</style>
"""


def init_state() -> None:
    defaults = {
        "completed_lessons": set(),
        "quiz_history": [],
        "writing_history": [],
        "learner_name": "学習者",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def html_card(title: str, body: str, tag: str | None = None) -> None:
    tag_html = f"<span class='tag'>{escape(tag)}</span>" if tag else ""
    st.markdown(
        f"""
        <div class="card">
          {tag_html}
          <h3>{escape(title)}</h3>
          <div class="card-body">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    completed = len(st.session_state.completed_lessons)
    total = len(LESSONS)
    best = max(
        [record["percent"] for record in st.session_state.quiz_history],
        default=0,
    )
    st.markdown(
        """
        <div class="hero">
          <div class="hero-title">がんばる日本語ラボ</div>
          <div class="hero-copy">
            「がんばって」だけに頼らず、相手の状況に合った励まし、共感、提案を練習します。
            場面を読み、表現を選び、自分の言葉で返答を作るところまで進めます。
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    left, middle, right = st.columns(3)
    left.metric("完了レッスン", f"{completed} / {total}")
    middle.metric("最高テスト結果", f"{best}%")
    right.metric("総練習記録", len(st.session_state.writing_history))
    st.progress(completed / total if total else 0)


def render_sidebar() -> tuple[str, str, str]:
    with st.sidebar:
        st.header("授業設定")
        learner_name = st.text_input(
            "学習者名",
            value=st.session_state.learner_name,
            help="進捗CSVに記録されます。",
        )
        st.session_state.learner_name = learner_name.strip() or "学習者"
        lesson_labels = {
            f"{lesson['title']} ({lesson['level']})": lesson["id"] for lesson in LESSONS
        }
        selected_label = st.selectbox("レッスン", list(lesson_labels.keys()))
        mode = st.radio(
            "表示モード",
            ["学習者向け", "教師向け"],
            horizontal=True,
        )
        quiz_scope = st.radio(
            "確認テスト",
            ["選択中のレッスン", "総合テスト"],
            horizontal=False,
        )
        st.divider()
        if st.button("進捗をリセット"):
            st.session_state.completed_lessons = set()
            st.session_state.quiz_history = []
            st.session_state.writing_history = []
            st.rerun()
        return lesson_labels[selected_label], mode, quiz_scope


def render_map() -> None:
    st.subheader("学習マップ")
    columns = st.columns(2)
    for index, lesson in enumerate(LESSONS):
        done = lesson["id"] in st.session_state.completed_lessons
        body = (
            f"<span class='tag'>{escape(lesson['duration'])}</span>"
            f"<span class='tag'>{escape(lesson['focus'])}</span>"
            f"<p>{'完了済み' if done else '未完了'}。"
            f"到達目標: {escape(lesson['goals'][0])}</p>"
        )
        with columns[index % 2]:
            html_card(lesson["title"], body, lesson["level"])

    st.divider()
    st.subheader("授業の流れ")
    col1, col2, col3 = st.columns(3)
    with col1:
        html_card(
            "1. 導入",
            "ウォームアップで経験を引き出し、例文で表現の役割を確認します。",
            "10分",
        )
    with col2:
        html_card(
            "2. 練習",
            "場面を選び、相手との関係に合う励ましを書いて保存します。",
            "15分",
        )
    with col3:
        html_card(
            "3. 確認",
            "選択式テストで理解を確認し、間違いは解説つきで復習します。",
            "10分",
        )


def render_lesson(lesson: dict[str, Any], mode: str) -> None:
    st.subheader(lesson["title"])
    st.caption(f"{lesson['level']} | {lesson['duration']} | {lesson['focus']}")

    goal_col, warmup_col = st.columns(2)
    with goal_col:
        st.markdown("#### 今日の目標")
        for goal in lesson["goals"]:
            st.checkbox(goal, key=f"goal_{lesson['id']}_{goal}")
    with warmup_col:
        st.markdown("#### ウォームアップ")
        for item in lesson["warmup"]:
            st.markdown(f"- {item}")

    st.markdown("#### 重要表現")
    key_columns = st.columns(3)
    for index, point in enumerate(lesson["key_points"]):
        with key_columns[index % 3]:
            html_card(point["label"], escape(point["body"]))

    st.markdown("#### 例文と使う場面")
    for example in lesson["examples"]:
        st.markdown(
            f"""
            <div class="example">
              <strong>{escape(example['scene'])}</strong><br>
              {escape(example['ja'])}<br>
              <span class="small-note">{escape(example['note'])}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if mode == "教師向け":
        with st.expander("教師用メモ", expanded=True):
            for note in lesson["teacher_notes"]:
                st.markdown(f"- {note}")

    if st.button("このレッスンを完了にする", key=f"done_{lesson['id']}"):
        st.session_state.completed_lessons.add(lesson["id"])
        st.success("完了として記録しました。")


def render_practice(lesson: dict[str, Any]) -> None:
    st.subheader("練習と振り返り")
    prompt = st.selectbox(
        "練習場面",
        lesson["practice_prompts"],
        key=f"prompt_{lesson['id']}",
    )
    response = st.text_area(
        "あなたの返答",
        height=140,
        placeholder="例: 大変だったね。今日は無理しないでね。話したくなったら聞くよ。",
        key=f"writing_{lesson['id']}",
    )

    st.markdown("#### セルフチェック")
    check_cols = st.columns(3)
    checks = []
    labels = [
        "相手の気持ちを受け止めた",
        "場面に合うていねいさにした",
        "次の行動や支援を入れた",
    ]
    for index, label in enumerate(labels):
        with check_cols[index]:
            checks.append(st.checkbox(label, key=f"check_{lesson['id']}_{index}"))

    if st.button("練習を保存", key=f"save_writing_{lesson['id']}"):
        if not response.strip():
            st.warning("返答を書いてから保存してください。")
        else:
            st.session_state.writing_history.append(
                {
                    "lesson_id": lesson["id"],
                    "lesson_title": lesson["title"],
                    "prompt": prompt,
                    "response": response.strip(),
                    "checks": sum(checks),
                    "date": datetime.now().isoformat(timespec="seconds"),
                }
            )
            st.success("練習記録を保存しました。")

    st.markdown("#### 評価ルーブリック")
    rubric_cols = st.columns(3)
    for index, item in enumerate(RUBRIC):
        with rubric_cols[index]:
            st.markdown(
                f"""
                <div class="rubric">
                  <strong>{escape(item['criterion'])}</strong><br>
                  <span class="small-note">到達: {escape(item['excellent'])}</span><br>
                  <span class="small-note">途中: {escape(item['developing'])}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if st.session_state.writing_history:
        with st.expander("保存済みの練習記録"):
            for record in reversed(st.session_state.writing_history[-5:]):
                st.markdown(
                    f"**{escape(record['lesson_title'])}** | {escape(record['date'])}"
                )
                st.markdown(f"- 場面: {escape(record['prompt'])}")
                st.markdown(f"- 返答: {escape(record['response'])}")


def questions_for_scope(lesson: dict[str, Any], quiz_scope: str) -> list[dict[str, Any]]:
    if quiz_scope == "総合テスト":
        return all_questions()
    return [
        {**question, "lesson_id": lesson["id"], "lesson_title": lesson["title"]}
        for question in lesson["quiz"]
    ]


def render_quiz(lesson: dict[str, Any], quiz_scope: str) -> None:
    st.subheader("確認テスト")
    questions = questions_for_scope(lesson, quiz_scope)
    scope_key = "all" if quiz_scope == "総合テスト" else lesson["id"]

    answers: dict[str, str] = {}
    with st.form(f"quiz_{scope_key}"):
        for index, question in enumerate(questions, start=1):
            st.markdown(f"**Q{index}. {question['question']}**")
            selected = st.radio(
                "回答",
                ["未選択"] + question["options"],
                key=f"answer_{scope_key}_{question['id']}",
                label_visibility="collapsed",
            )
            answers[question["id"]] = selected
        submitted = st.form_submit_button("採点する")

    if not submitted:
        st.info("回答を選んでから採点してください。")
        return

    if any(value == "未選択" for value in answers.values()):
        st.warning("未選択の問題があります。すべて選んでから採点してください。")
        return

    result = score_answers(questions, answers)
    st.session_state.quiz_history.append(
        {
            "scope": quiz_scope if quiz_scope == "総合テスト" else lesson["title"],
            "correct": result["correct"],
            "total": result["total"],
            "percent": result["percent"],
            "date": datetime.now().isoformat(timespec="seconds"),
        }
    )

    st.metric("結果", f"{result['correct']} / {result['total']}", f"{result['percent']}%")
    if result["percent"] >= 80:
        st.success("理解は十分です。次は会話練習で使えるか確認しましょう。")
    else:
        st.warning("解説を読んで、もう一度レッスンの例文を確認しましょう。")

    for row in result["rows"]:
        status = "正解" if row["correct"] else "要復習"
        css_class = "correct" if row["correct"] else "incorrect"
        st.markdown(
            f"""
            <div class="card">
              <span class="{css_class}">{status}</span>
              <p><strong>{escape(row['question'])}</strong></p>
              <p>あなたの回答: {escape(row['selected'])}</p>
              <p>正答: {escape(row['answer'])}</p>
              <p class="small-note">{escape(row['explain'])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_materials(lesson: dict[str, Any]) -> None:
    st.subheader("教材出力")
    st.write("授業で使う配布資料、教師用ガイド、進捗記録をまとめます。")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            "ワークシートを出力",
            build_worksheet(lesson),
            file_name=f"{lesson['id']}_worksheet.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with col2:
        st.download_button(
            "教師用ガイドを出力",
            build_teacher_guide(),
            file_name="teacher_guide.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with col3:
        st.download_button(
            "進捗CSVを出力",
            build_progress_csv(
                st.session_state.learner_name,
                st.session_state.completed_lessons,
                st.session_state.quiz_history,
                st.session_state.writing_history,
            ),
            file_name="progress.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with st.expander("出力されるワークシートのプレビュー", expanded=True):
        st.code(build_worksheet(lesson), language="text")


def main() -> None:
    init_state()
    st.markdown(CSS, unsafe_allow_html=True)
    selected_lesson_id, mode, quiz_scope = render_sidebar()
    lesson = get_lesson(selected_lesson_id)
    render_hero()

    map_tab, lesson_tab, practice_tab, quiz_tab, materials_tab = st.tabs(
        ["学習マップ", "レッスン", "練習", "確認テスト", "教材出力"]
    )
    with map_tab:
        render_map()
    with lesson_tab:
        render_lesson(lesson, mode)
    with practice_tab:
        render_practice(lesson)
    with quiz_tab:
        render_quiz(lesson, quiz_scope)
    with materials_tab:
        render_materials(lesson)


if __name__ == "__main__":
    main()
