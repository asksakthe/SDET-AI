# AI Document Pipeline

A Python pipeline that reads documents, splits them into chunks,
and uses an LLM to summarise each chunk.

Built as part of my AI Engineer transition journey.

## What it does
1. Reads a text document from disk
2. Cleans and splits it into overlapping chunks
3. Sends each chunk to Groq LLM API for summarisation
4. Returns structured results with original text and AI summary

## Tech stack
- Python 3.10+
- Groq API (LLaMA 3)
- No frameworks — pure Python pipeline

## How to run
1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Set your Groq API key: export GROQ_API_KEY=your_key_here
4. Run: python main.py

## Project structure
- pipeline/file_handler.py  — reads files from disk
- pipeline/chunker.py       — cleans and chunks text
- pipeline/llm_caller.py    — calls Groq LLM API safely
- pipeline/ai_pipeline.py   — orchestrates the full pipeline

## What I learned building this
- Modular Python programming
- File handling and text processing
- LLM API integration
- Object-oriented pipeline design
- Error handling and defensive coding