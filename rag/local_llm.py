import subprocess


def generate_answer(prompt):

    result = subprocess.run(
        [
            "ollama",
            "run",
            "llama3.2:3b"
        ],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    return result.stdout