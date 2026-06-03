from __future__ import annotations

import csv
import io
from datetime import datetime
from typing import Any


LESSONS: list[dict[str, Any]] = [
    {
        "id": "lesson_1",
        "level": "初級",
        "title": "「がんばる」の基本",
        "duration": "25分",
        "focus": "意味、形、自然に使える場面",
        "goals": [
            "「がんばる」「がんばって」「がんばっています」の違いを説明できる",
            "自分の予定や目標を使って短い文を作れる",
            "相手を応援する一言を場面に合わせて選べる",
        ],
        "warmup": [
            "最近がんばったことを一つ書く",
            "そのとき、だれにどんな言葉をかけてもらいたかったか話す",
        ],
        "key_points": [
            {
                "label": "がんばる",
                "body": "自分が努力することを表す。例: 日本語の勉強をがんばります。",
            },
            {
                "label": "がんばって",
                "body": "相手を応援する表現。近い相手には自然だが、強いプレッシャーになる場面もある。",
            },
            {
                "label": "がんばっています",
                "body": "今、継続して努力している状態を表す。例: 毎日発音の練習をがんばっています。",
            },
        ],
        "examples": [
            {
                "scene": "試験前",
                "ja": "明日の試験、がんばってください。",
                "note": "ていねいな応援。先生から学生にも使える。",
            },
            {
                "scene": "自己紹介",
                "ja": "今年は漢字の勉強をがんばりたいです。",
                "note": "目標を話すときの自然な形。",
            },
            {
                "scene": "進捗報告",
                "ja": "発音はまだ難しいですが、毎日がんばっています。",
                "note": "努力が続いていることを伝える。",
            },
        ],
        "practice_prompts": [
            "あなたが今がんばっていることを一文で書きましょう。",
            "友だちが明日テストを受けます。自然な応援の一言を書きましょう。",
            "先生に自分の学習目標をていねいに伝えましょう。",
        ],
        "quiz": [
            {
                "id": "l1_q1",
                "question": "自分の目標を話す文として最も自然なものはどれですか。",
                "options": [
                    "今年は会話の練習をがんばりたいです。",
                    "今年は会話の練習をがんばってください。",
                    "今年は会話の練習をがんばっていますください。",
                ],
                "answer": "今年は会話の練習をがんばりたいです。",
                "explain": "自分の目標は「がんばりたいです」が自然です。",
            },
            {
                "id": "l1_q2",
                "question": "相手を応援するときに使う表現はどれですか。",
                "options": ["がんばってください。", "がんばりたいです。", "がんばっています。"],
                "answer": "がんばってください。",
                "explain": "相手への応援は「がんばってください」が基本形です。",
            },
            {
                "id": "l1_q3",
                "question": "「毎日ピアノを練習しています」と近い意味の文はどれですか。",
                "options": [
                    "ピアノの練習をがんばっています。",
                    "ピアノの練習をがんばってください。",
                    "ピアノの練習をがんばりませんください。",
                ],
                "answer": "ピアノの練習をがんばっています。",
                "explain": "継続して努力している状態は「がんばっています」で表せます。",
            },
        ],
        "teacher_notes": [
            "最初に「努力」と「応援」の二つの意味を分けて板書する。",
            "学生の母語で直訳しすぎず、場面と相手との関係で判断させる。",
            "「がんばって」は便利だが、つらい相手には別表現が必要なことも導入する。",
        ],
    },
    {
        "id": "lesson_2",
        "level": "初級から中級",
        "title": "励ましの言い換え",
        "duration": "30分",
        "focus": "相手に負担をかけにくい応援表現",
        "goals": [
            "「がんばって」以外の励ましを3つ以上使える",
            "相手の状態に合わせて、やさしい言い方を選べる",
            "励まし、共感、提案の違いを見分けられる",
        ],
        "warmup": [
            "「がんばって」と言われてうれしい場面、少し重い場面を分ける",
            "同じ場面で別の言い方を考える",
        ],
        "key_points": [
            {
                "label": "応援しているよ",
                "body": "相手を支える気持ちを伝える。直接プレッシャーをかけにくい。",
            },
            {
                "label": "無理しないでね",
                "body": "相手が疲れているときに使う。努力より体調を大切にする言い方。",
            },
            {
                "label": "一緒にやろう",
                "body": "相手だけに努力を求めず、協力する姿勢を示す。",
            },
        ],
        "examples": [
            {
                "scene": "友人が疲れている",
                "ja": "大変だったね。今日は無理しないでね。",
                "note": "共感してから言うと自然。",
            },
            {
                "scene": "友人が発表前で不安",
                "ja": "準備してきたから大丈夫。応援しているよ。",
                "note": "事実を添えると安心感が出る。",
            },
            {
                "scene": "課題が進まない",
                "ja": "一人で大変なら、次の部分は一緒にやろう。",
                "note": "具体的に手伝う提案。",
            },
        ],
        "practice_prompts": [
            "疲れている友だちに、やさしい一言を書きましょう。",
            "発表前のクラスメイトに、プレッシャーをかけにくい応援を書きましょう。",
            "困っている相手に、共感と提案を入れて返事を書きましょう。",
        ],
        "quiz": [
            {
                "id": "l2_q1",
                "question": "相手がかなり疲れているとき、最も自然な表現はどれですか。",
                "options": ["無理しないでね。", "もっとがんばって。", "早く終わって。"],
                "answer": "無理しないでね。",
                "explain": "疲れている相手には、努力を求めるより体調を気づかう表現が自然です。",
            },
            {
                "id": "l2_q2",
                "question": "「一緒にやろう」の主な効果はどれですか。",
                "options": [
                    "協力する気持ちを伝えられる",
                    "相手の失敗を強く責められる",
                    "相手を一人にできる",
                ],
                "answer": "協力する気持ちを伝えられる",
                "explain": "「一緒にやろう」は相手の負担を下げる言い方です。",
            },
            {
                "id": "l2_q3",
                "question": "発表前で不安な友人に合う一言はどれですか。",
                "options": [
                    "準備してきたから大丈夫。応援しているよ。",
                    "失敗したら困るね。",
                    "発表はやめたほうがいいよ。",
                ],
                "answer": "準備してきたから大丈夫。応援しているよ。",
                "explain": "安心材料と応援をセットで伝えると自然です。",
            },
        ],
        "teacher_notes": [
            "「応援」「共感」「提案」のラベルを使って表現を整理する。",
            "正解を一つに固定せず、場面に合う理由を説明させる。",
            "ロールプレイでは声のトーンや表情も評価に入れる。",
        ],
    },
    {
        "id": "lesson_3",
        "level": "中級",
        "title": "場面別ロールプレイ",
        "duration": "35分",
        "focus": "学校、仕事、友人関係での自然な会話",
        "goals": [
            "相手との関係に合わせて、ていねいさを調整できる",
            "会話を2往復以上続けられる",
            "励ましのあとに具体的な行動を提案できる",
        ],
        "warmup": [
            "先生、友人、先輩に言うときの違いを考える",
            "同じ内容をカジュアル、ていねいの二つで言い換える",
        ],
        "key_points": [
            {
                "label": "ていねいさ",
                "body": "先生や先輩には「がんばってください」「応援しています」が使いやすい。",
            },
            {
                "label": "会話の続け方",
                "body": "励ましだけで終わらず、「何か手伝えることがありますか」と続ける。",
            },
            {
                "label": "具体性",
                "body": "「資料を一緒に確認しましょう」のように具体的な行動を入れる。",
            },
        ],
        "examples": [
            {
                "scene": "先生に研究発表前の応援",
                "ja": "明日の発表、応援しています。準備がうまくいくことを願っています。",
                "note": "目上の相手には落ち着いた表現が自然。",
            },
            {
                "scene": "同級生に課題の相談",
                "ja": "大変そうだね。よかったら、資料の整理を一緒にしようか。",
                "note": "共感から具体的な手伝いへ進む。",
            },
            {
                "scene": "アルバイト先",
                "ja": "初日で緊張しますよね。わからないことがあれば聞いてください。",
                "note": "職場では具体的に支援を伝えるとよい。",
            },
        ],
        "practice_prompts": [
            "先生が大きな発表をします。ていねいな応援を2文で書きましょう。",
            "同級生が課題で困っています。共感と提案を入れて2往復の会話を書きましょう。",
            "アルバイト先の後輩に、安心できる一言を書きましょう。",
        ],
        "quiz": [
            {
                "id": "l3_q1",
                "question": "先生に対する表現として最も自然なのはどれですか。",
                "options": ["応援しています。", "まあ、がんばって。", "早くやってね。"],
                "answer": "応援しています。",
                "explain": "目上の相手には、落ち着いたていねいな表現が自然です。",
            },
            {
                "id": "l3_q2",
                "question": "励ましのあとに会話を続ける表現としてよいものはどれですか。",
                "options": [
                    "何か手伝えることがありますか。",
                    "それはあなたの問題です。",
                    "もう話さないでください。",
                ],
                "answer": "何か手伝えることがありますか。",
                "explain": "支援の意志を具体的に伝えると会話が続きます。",
            },
            {
                "id": "l3_q3",
                "question": "同級生へのカジュアルな提案として自然なのはどれですか。",
                "options": [
                    "よかったら一緒に確認しよう。",
                    "確認なさってくださいませ。",
                    "確認してはいけません。",
                ],
                "answer": "よかったら一緒に確認しよう。",
                "explain": "同級生には自然でやわらかいカジュアル表現が使えます。",
            },
        ],
        "teacher_notes": [
            "ペア練習は役割カードを配って、相手との関係を明確にする。",
            "発話の正確さだけでなく、相手への配慮と会話の継続も見る。",
            "発表後は、よかった表現を全体で共有する。",
        ],
    },
    {
        "id": "lesson_4",
        "level": "中級から上級",
        "title": "配慮が必要な励まし",
        "duration": "40分",
        "focus": "相手の負担を下げる言い方とフィードバック",
        "goals": [
            "「がんばって」が合わない場面を判断できる",
            "相手の状況を受け止める一文を先に言える",
            "励ましと助言を区別して、自然な順序で話せる",
        ],
        "warmup": [
            "落ち込んでいる人に言わないほうがよい表現を考える",
            "共感、確認、提案の順番で短い会話を作る",
        ],
        "key_points": [
            {
                "label": "先に受け止める",
                "body": "「大変だったね」「つらかったですね」のように、相手の気持ちを認める。",
            },
            {
                "label": "押しつけない",
                "body": "すぐに解決策を出すより、「話したいときは聞くよ」と選択肢を渡す。",
            },
            {
                "label": "小さな次の一歩",
                "body": "大きな努力ではなく、「今日は休もう」「一つだけ確認しよう」と小さくする。",
            },
        ],
        "examples": [
            {
                "scene": "試験に落ちた友人",
                "ja": "つらかったね。今は少し休んでもいいと思う。話したくなったら聞くよ。",
                "note": "すぐに励ますより受け止めを優先。",
            },
            {
                "scene": "仕事で失敗した同僚",
                "ja": "大変でしたね。次にできることを一緒に整理しましょうか。",
                "note": "共感から提案へ進む。",
            },
            {
                "scene": "やる気が出ない学習者",
                "ja": "今日は一つだけ例文を確認しましょう。できたら十分です。",
                "note": "小さな達成に変える。",
            },
        ],
        "practice_prompts": [
            "落ち込んでいる友だちに、共感を先にした返事を書きましょう。",
            "失敗した同僚に、助言を押しつけない言い方で返しましょう。",
            "やる気が出ない学習者に、小さな次の一歩を提案しましょう。",
        ],
        "quiz": [
            {
                "id": "l4_q1",
                "question": "落ち込んでいる相手に最初に言う表現として自然なのはどれですか。",
                "options": ["つらかったね。", "もっと努力しないと。", "気にしないで早く忘れて。"],
                "answer": "つらかったね。",
                "explain": "まず相手の気持ちを受け止める表現が自然です。",
            },
            {
                "id": "l4_q2",
                "question": "助言を押しつけにくい表現はどれですか。",
                "options": [
                    "次にできることを一緒に整理しましょうか。",
                    "私の言う通りにしてください。",
                    "あなたは間違っています。",
                ],
                "answer": "次にできることを一緒に整理しましょうか。",
                "explain": "「しましょうか」は相手に選択の余地を残します。",
            },
            {
                "id": "l4_q3",
                "question": "やる気が出ない学習者への支援としてよいものはどれですか。",
                "options": [
                    "今日は一つだけ例文を確認しましょう。",
                    "全部終わるまで休んではいけません。",
                    "できないならやめてください。",
                ],
                "answer": "今日は一つだけ例文を確認しましょう。",
                "explain": "負担を小さくし、達成しやすい次の行動にするのが有効です。",
            },
        ],
        "teacher_notes": [
            "センシティブな場面では、正解探しより理由づけを重視する。",
            "学生の実体験を扱う場合は、共有の強制をしない。",
            "「共感、確認、提案」の順番をテンプレートとして練習する。",
        ],
    },
]


RUBRIC: list[dict[str, str]] = [
    {
        "criterion": "場面理解",
        "excellent": "相手の状態と関係に合った表現を選べている",
        "developing": "表現は伝わるが、場面への配慮が少ない",
    },
    {
        "criterion": "日本語の自然さ",
        "excellent": "文法、ていねいさ、語順が自然で聞き取りやすい",
        "developing": "意味は分かるが、形やていねいさに修正が必要",
    },
    {
        "criterion": "支援の具体性",
        "excellent": "励ましのあとに具体的な行動や選択肢がある",
        "developing": "励ましだけで終わり、次の行動が見えにくい",
    },
]


def get_lesson(lesson_id: str) -> dict[str, Any]:
    for lesson in LESSONS:
        if lesson["id"] == lesson_id:
            return lesson
    raise KeyError(f"Unknown lesson id: {lesson_id}")


def all_questions() -> list[dict[str, Any]]:
    return [
        {**question, "lesson_id": lesson["id"], "lesson_title": lesson["title"]}
        for lesson in LESSONS
        for question in lesson["quiz"]
    ]


def score_answers(
    questions: list[dict[str, Any]], answers: dict[str, str]
) -> dict[str, Any]:
    rows = []
    correct_count = 0
    for question in questions:
        selected = answers.get(question["id"], "")
        is_correct = selected == question["answer"]
        correct_count += int(is_correct)
        rows.append(
            {
                "id": question["id"],
                "lesson": question.get("lesson_title", ""),
                "question": question["question"],
                "selected": selected,
                "answer": question["answer"],
                "correct": is_correct,
                "explain": question["explain"],
            }
        )

    total = len(questions)
    percent = round((correct_count / total) * 100) if total else 0
    return {
        "correct": correct_count,
        "total": total,
        "percent": percent,
        "rows": rows,
    }


def build_worksheet(lesson: dict[str, Any]) -> str:
    lines = [
        f"教材: {lesson['title']}",
        f"レベル: {lesson['level']}",
        f"時間: {lesson['duration']}",
        "",
        "1. 今日の目標",
    ]
    lines.extend(f"- {goal}" for goal in lesson["goals"])
    lines.extend(["", "2. ウォームアップ"])
    lines.extend(f"- {item}" for item in lesson["warmup"])
    lines.extend(["", "3. 重要表現"])
    for point in lesson["key_points"]:
        lines.append(f"- {point['label']}: {point['body']}")
    lines.extend(["", "4. 例文"])
    for example in lesson["examples"]:
        lines.append(f"- [{example['scene']}] {example['ja']}")
        lines.append(f"  メモ: {example['note']}")
    lines.extend(["", "5. 練習"])
    for index, prompt in enumerate(lesson["practice_prompts"], start=1):
        lines.append(f"{index}. {prompt}")
        lines.append("   回答: ______________________________________________")
    lines.extend(["", "6. 振り返り", "- 今日使えるようになった表現:", "- 次に練習したい場面:"])
    return "\n".join(lines)


def build_teacher_guide() -> str:
    lines = [
        "がんばる日本語ラボ 教師用ガイド",
        "",
        "授業の流れ",
        "1. 場面を提示して、表現を予想させる",
        "2. 例文で意味、ていねいさ、相手への配慮を確認する",
        "3. ペアでロールプレイを行う",
        "4. 確認テストで理解を見える化する",
        "5. 振り返りで次回の課題を決める",
        "",
        "レッスン別メモ",
    ]
    for lesson in LESSONS:
        lines.extend(["", f"{lesson['title']} ({lesson['duration']})"])
        lines.extend(f"- {note}" for note in lesson["teacher_notes"])
    lines.extend(["", "評価ルーブリック"])
    for item in RUBRIC:
        lines.append(
            f"- {item['criterion']}: 到達例「{item['excellent']}」 / 途中段階「{item['developing']}」"
        )
    return "\n".join(lines)


def build_progress_csv(
    learner_name: str,
    completed_lessons: set[str],
    quiz_history: list[dict[str, Any]],
    writing_history: list[dict[str, Any]],
) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["exported_at", datetime.now().isoformat(timespec="seconds")])
    writer.writerow(["learner_name", learner_name])
    writer.writerow([])
    writer.writerow(["completed_lesson_id", "completed_lesson_title"])
    for lesson_id in sorted(completed_lessons):
        lesson = get_lesson(lesson_id)
        writer.writerow([lesson_id, lesson["title"]])
    writer.writerow([])
    writer.writerow(["quiz_scope", "score", "total", "percent", "date"])
    for record in quiz_history:
        writer.writerow(
            [
                record["scope"],
                record["correct"],
                record["total"],
                record["percent"],
                record["date"],
            ]
        )
    writer.writerow([])
    writer.writerow(["lesson", "prompt", "response", "date"])
    for record in writing_history:
        writer.writerow(
            [
                record["lesson_title"],
                record["prompt"],
                record["response"],
                record["date"],
            ]
        )
    return buffer.getvalue()

