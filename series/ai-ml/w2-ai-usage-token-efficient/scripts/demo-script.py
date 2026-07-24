#!/usr/bin/env python3
"""
Demo Script: Token-Efficient AI Workflows
Workshop 2 - AI Usage Token Efficiency

This script demonstrates token counting, prompt efficiency,
and workflow optimization techniques.

Usage:
    python demo-script.py
"""

import tiktoken
from datetime import datetime
from typing import List, Dict, Any
import json


# ============================================================================
# DEMO 1: Token Counting Basics
# ============================================================================

def demo_token_counting():
    """Demonstrate how tokenization works."""
    print("=" * 70)
    print("DEMO 1: Understanding Tokens")
    print("=" * 70)
    
    encoder = tiktoken.encoding_for_model("gpt-4")
    
    examples = [
        ("Hello, world!", "Simple greeting"),
        ("Hello,world!", "No space after comma"),
        ("artificial intelligence", "Common phrase"),
        ("AI", "Abbreviation"),
        ("console.log('test')", "JavaScript code"),
        ("café", "Non-ASCII characters"),
        ("🚀", "Emoji"),
        ("def hello():\n    print('hi')", "Python code"),
    ]
    
    print("\nTokenization Examples:\n")
    print(f"{'Text':<30} {'Chars':<6} {'Tokens':<7} {'Note':<25}")
    print("-" * 70)
    
    for text, note in examples:
        token_count = len(encoder.encode(text))
        char_count = len(text)
        print(f"{text:<30} {char_count:<6} {token_count:<7} {note:<25}")
    
    # Show token IDs for one example
    print("\n" + "=" * 70)
    print("Token IDs for 'Hello, world!':")
    tokens = encoder.encode("Hello, world!")
    print(f"Token IDs: {tokens}")
    print(f"Decoded: {[encoder.decode([t]) for t in tokens]}")
    
    input("\nPress Enter to continue...")


# ============================================================================
# DEMO 2: Code Verbosity and Token Cost
# ============================================================================

def demo_code_verbosity():
    """Show how different code styles affect token count."""
    print("\n" + "=" * 70)
    print("DEMO 2: Code Verbosity Impact on Tokens")
    print("=" * 70)
    
    encoder = tiktoken.encoding_for_model("gpt-4")
    
    code_samples = {
        "Minimal": """
def add(a, b):
    return a + b
""",
        "With Type Hints": """
def add(a: int, b: int) -> int:
    return a + b
""",
        "With Docstring": """
def add(a: int, b: int) -> int:
    \"\"\"Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    \"\"\"
    return a + b
""",
        "Production Ready": """
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    \"\"\"Add two numbers with comprehensive type checking.
    
    This function performs addition on numeric inputs with proper
    type validation and error handling.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        Sum of a and b
        
    Raises:
        TypeError: If either argument is not a number
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.7)
        6.2
    \"\"\"
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number, got {type(a)}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number, got {type(b)}")
    return a + b
"""
    }
    
    print("\nToken costs for different code styles:\n")
    print(f"{'Style':<20} {'Lines':<7} {'Chars':<7} {'Tokens':<8} {'Multiplier':<10}")
    print("-" * 70)
    
    baseline_tokens = 0
    for i, (style, code) in enumerate(code_samples.items()):
        lines = len(code.strip().split('\n'))
        chars = len(code)
        tokens = len(encoder.encode(code))
        
        if i == 0:
            baseline_tokens = tokens
            multiplier = "1.0x"
        else:
            multiplier = f"{tokens / baseline_tokens:.1f}x"
        
        print(f"{style:<20} {lines:<7} {chars:<7} {tokens:<8} {multiplier:<10}")
    
    print("\n💡 Key Insight:")
    print("   Ask AI for minimal working code first.")
    print("   Add documentation in a second step if needed.")
    print("   This allows you to test functionality before investing in polish.")
    
    input("\nPress Enter to continue...")


# ============================================================================
# DEMO 3: Prompt Efficiency Comparison
# ============================================================================

def demo_prompt_efficiency():
    """Compare token costs of different prompting styles."""
    print("\n" + "=" * 70)
    print("DEMO 3: Prompt Efficiency")
    print("=" * 70)
    
    encoder = tiktoken.encoding_for_model("gpt-4")
    
    prompts = {
        "❌ Over-engineered": """
Act as an expert senior software engineer with over 20 years of experience 
in building scalable, distributed systems. You have deep expertise in Python, 
JavaScript, Go, and Rust. You always follow SOLID principles, clean 
architecture, and domain-driven design. You are meticulous about code quality, 
security, and performance. You write comprehensive tests and documentation.
You think step by step, considering all edge cases and potential issues.

Please create a highly robust, production-ready, enterprise-grade user 
registration system that follows all best practices, includes comprehensive 
error handling, security measures, and is fully tested.
""",
        
        "❌ Too vague": """
Create a user registration system
""",
        
        "✅ Clear and specific": """
Create a function register_user(email: str, password: str) that:
1. Validates email format (contains @)
2. Validates password length (min 8 chars)
3. Returns dict with 'success' (bool) and 'message' (str)
4. No database - just validation
Max 20 lines
"""
    }
    
    print("\nToken costs for different prompting styles:\n")
    print(f"{'Style':<25} {'Tokens':<8} {'Efficiency':<15}")
    print("-" * 70)
    
    for style, prompt in prompts.items():
        tokens = len(encoder.encode(prompt))
        if "✅" in style:
            efficiency = "EFFICIENT ⭐"
        else:
            efficiency = "WASTEFUL"
        print(f"{style:<25} {tokens:<8} {efficiency:<15}")
    
    # Calculate savings
    wasteful = len(encoder.encode(prompts["❌ Over-engineered"]))
    efficient = len(encoder.encode(prompts["✅ Clear and specific"]))
    savings = ((wasteful - efficient) / wasteful) * 100
    
    print(f"\n💰 Token Savings: {savings:.1f}%")
    print(f"   Over-engineered: {wasteful} tokens")
    print(f"   Clear & specific: {efficient} tokens")
    print(f"   Saved: {wasteful - efficient} tokens per request")
    
    input("\nPress Enter to continue...")


# ============================================================================
# DEMO 4: Incremental vs. Monolithic Token Costs
# ============================================================================

def demo_incremental_vs_monolithic():
    """Simulate token costs for different development approaches."""
    print("\n" + "=" * 70)
    print("DEMO 4: Incremental vs. Monolithic Workflows")
    print("=" * 70)
    
    print("\nScenario: Building a TODO API")
    print("-" * 70)
    
    # Monolithic approach
    monolithic = {
        "prompt": "Create a complete Flask TODO API with task model, storage, CRUD endpoints, validation, and tests",
        "estimated_context": 5000,  # AI loads lots of context
        "estimated_response": 3500,  # Generates lots of code
        "iterations": 3,  # Needs debugging
    }
    
    monolithic_total = (
        len(monolithic["prompt"]) // 4 +  # Rough token estimate
        monolithic["estimated_context"] +
        monolithic["estimated_response"]
    ) * monolithic["iterations"]
    
    # Incremental approach
    incremental_steps = [
        {"name": "Task model", "prompt_tokens": 60, "response_tokens": 150, "context": 500},
        {"name": "TaskStore", "prompt_tokens": 70, "response_tokens": 180, "context": 600},
        {"name": "POST endpoint", "prompt_tokens": 90, "response_tokens": 220, "context": 800},
        {"name": "Validation", "prompt_tokens": 80, "response_tokens": 120, "context": 900},
        {"name": "GET endpoint", "prompt_tokens": 60, "response_tokens": 100, "context": 1000},
    ]
    
    incremental_total = sum(
        step["prompt_tokens"] + step["response_tokens"] + step["context"]
        for step in incremental_steps
    )
    
    # Display comparison
    print("\n🔴 Monolithic Approach:")
    print(f"   Single prompt: ~{len(monolithic['prompt']) // 4} tokens")
    print(f"   Context loaded: ~{monolithic['estimated_context']} tokens")
    print(f"   Response: ~{monolithic['estimated_response']} tokens")
    print(f"   Iterations: {monolithic['iterations']} (debugging)")
    print(f"   TOTAL: ~{monolithic_total:,} tokens")
    
    print("\n🟢 Incremental Approach:")
    for i, step in enumerate(incremental_steps, 1):
        total = step["prompt_tokens"] + step["response_tokens"] + step["context"]
        print(f"   Step {i} ({step['name']:<15}): {total:4} tokens")
    print(f"   TOTAL: ~{incremental_total:,} tokens")
    
    savings = ((monolithic_total - incremental_total) / monolithic_total) * 100
    print(f"\n💰 Savings: {savings:.1f}%")
    print(f"   Monolithic: {monolithic_total:,} tokens")
    print(f"   Incremental: {incremental_total:,} tokens")
    print(f"   Saved: {monolithic_total - incremental_total:,} tokens")
    
    # Cost calculation
    cost_per_million = 10  # GPT-4 input pricing (example)
    monolithic_cost = (monolithic_total / 1_000_000) * cost_per_million
    incremental_cost = (incremental_total / 1_000_000) * cost_per_million
    
    print(f"\n💵 Cost Comparison (at ${cost_per_million}/1M tokens):")
    print(f"   Monolithic: ${monolithic_cost:.4f}")
    print(f"   Incremental: ${incremental_cost:.4f}")
    print(f"   Saved: ${monolithic_cost - incremental_cost:.4f}")
    
    input("\nPress Enter to continue...")


# ============================================================================
# DEMO 5: Context Loading Efficiency
# ============================================================================

def demo_context_efficiency():
    """Show impact of loading full files vs. targeted context."""
    print("\n" + "=" * 70)
    print("DEMO 5: Context Loading Efficiency")
    print("=" * 70)
    
    encoder = tiktoken.encoding_for_model("gpt-4")
    
    # Simulate a file
    sample_file = """
# utils.py
from typing import List, Dict, Optional
import re
from datetime import datetime

def validate_email(email: str) -> bool:
    \"\"\"Validate email format.\"\"\"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password: str) -> bool:
    \"\"\"Validate password strength.\"\"\"
    return len(password) >= 8

def hash_password(password: str) -> str:
    \"\"\"Hash password using SHA256.\"\"\"
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

def format_date(date: datetime) -> str:
    \"\"\"Format datetime to ISO string.\"\"\"
    return date.isoformat()

def parse_date(date_str: str) -> datetime:
    \"\"\"Parse ISO date string.\"\"\"
    return datetime.fromisoformat(date_str)

# ... 20 more utility functions ...
""" * 3  # Simulate a larger file
    
    # Scenario: User wants to update validate_email
    
    # ❌ Bad: Load entire file
    prompt_full = f"""
Here's the entire utils.py file:

{sample_file}

Update the validate_email function to also reject emails with + signs.
"""
    
    # ✅ Good: Targeted request
    prompt_targeted = """
In utils.py, update validate_email to reject emails containing + signs.
"""
    
    tokens_full = len(encoder.encode(prompt_full))
    tokens_targeted = len(encoder.encode(prompt_targeted))
    
    print("\nScenario: Update email validation in utils.py")
    print("-" * 70)
    print(f"\n❌ Loading full file in prompt:")
    print(f"   Tokens: {tokens_full}")
    print(f"   (File pasted into prompt)")
    
    print(f"\n✅ Targeted file reference:")
    print(f"   Tokens: {tokens_targeted}")
    print(f"   (AI loads file automatically)")
    
    savings = ((tokens_full - tokens_targeted) / tokens_full) * 100
    print(f"\n💰 Savings: {savings:.1f}%")
    print(f"   Saved: {tokens_full - tokens_targeted} tokens")
    
    print("\n💡 Best Practice:")
    print("   Reference files by path, let AI load them.")
    print("   Don't paste file contents in your prompt.")
    
    input("\nPress Enter to continue...")


# ============================================================================
# DEMO 6: Agentic Token Costs
# ============================================================================

def demo_agentic_costs():
    """Demonstrate token costs in agentic workflows."""
    print("\n" + "=" * 70)
    print("DEMO 6: Agentic AI Token Costs")
    print("=" * 70)
    
    print("\nSimulating an agentic workflow...")
    print("Task: 'Add logging to my application'")
    print("-" * 70)
    
    # Simulate agentic steps
    steps = [
        {
            "step": "Planning",
            "action": "Agent analyzes the task and creates a plan",
            "tokens": 800
        },
        {
            "step": "Search codebase",
            "action": "Tool: search_files('logging')",
            "tokens": 3000
        },
        {
            "step": "Read main files",
            "action": "Tool: read_file('app.py'), read_file('config.py')",
            "tokens": 4500
        },
        {
            "step": "Check existing logging",
            "action": "Tool: grep_search('logger')",
            "tokens": 2000
        },
        {
            "step": "Generate logging config",
            "action": "AI generates logging configuration",
            "tokens": 1200
        },
        {
            "step": "Update files",
            "action": "Tool: write_file('config.py'), write_file('app.py')",
            "tokens": 2500
        },
        {
            "step": "Run tests",
            "action": "Tool: run_command('pytest')",
            "tokens": 1500
        },
        {
            "step": "Check test results",
            "action": "Read test output and verify",
            "tokens": 1000
        },
    ]
    
    print("\nAgent Execution Trace:\n")
    total = 0
    for i, step_info in enumerate(steps, 1):
        print(f"{i}. {step_info['step']:<20} {step_info['tokens']:>6} tokens")
        print(f"   {step_info['action']}")
        total += step_info["tokens"]
    
    print(f"\n{'='*40}")
    print(f"TOTAL TOKENS: {total:,}")
    print(f"{'='*40}")
    
    # Compare to supervised approach
    supervised_total = 2500
    
    print(f"\n📊 Comparison:\n")
    print(f"   Autonomous Agent: {total:,} tokens")
    print(f"   Supervised (step-by-step): {supervised_total:,} tokens")
    
    savings = ((total - supervised_total) / total) * 100
    print(f"\n💰 Supervision Savings: {savings:.1f}%")
    
    print("\n💡 Lesson:")
    print("   Agentic autonomy is powerful but expensive.")
    print("   Use supervision to control costs:")
    print("   - Request plans before execution")
    print("   - Set boundaries (which files to read)")
    print("   - Approve steps incrementally")
    
    input("\nPress Enter to continue...")


# ============================================================================
# DEMO 7: Cost Calculator
# ============================================================================

def demo_cost_calculator():
    """Calculate real-world costs based on usage patterns."""
    print("\n" + "=" * 70)
    print("DEMO 7: Token Cost Calculator")
    print("=" * 70)
    
    # Pricing (example, as of 2024)
    pricing = {
        "GPT-4 Turbo": {"input": 10, "output": 30},
        "GPT-4o": {"input": 5, "output": 15},
        "Claude 3.5 Sonnet": {"input": 3, "output": 15},
        "Claude 3 Opus": {"input": 15, "output": 75},
    }
    
    # Usage scenarios
    scenarios = {
        "Inefficient Developer": {
            "requests_per_day": 50,
            "avg_input_tokens": 8000,
            "avg_output_tokens": 3000,
        },
        "Efficient Developer": {
            "requests_per_day": 50,
            "avg_input_tokens": 2000,
            "avg_output_tokens": 800,
        }
    }
    
    print("\n📊 Monthly Cost Comparison\n")
    print(f"{'Model':<20} {'Inefficient':<15} {'Efficient':<15} {'Savings':<15}")
    print("-" * 70)
    
    for model, prices in pricing.items():
        costs = {}
        for scenario_name, usage in scenarios.items():
            monthly_input_tokens = usage["requests_per_day"] * usage["avg_input_tokens"] * 30
            monthly_output_tokens = usage["requests_per_day"] * usage["avg_output_tokens"] * 30
            
            cost = (
                (monthly_input_tokens / 1_000_000) * prices["input"] +
                (monthly_output_tokens / 1_000_000) * prices["output"]
            )
            costs[scenario_name] = cost
        
        savings = costs["Inefficient Developer"] - costs["Efficient Developer"]
        print(f"{model:<20} ${costs['Inefficient Developer']:>6.2f}         ${costs['Efficient Developer']:>6.2f}         ${savings:>6.2f}")
    
    print("\n💡 Annual Savings (Efficient vs. Inefficient):\n")
    for model, prices in pricing.items():
        inefficient = (
            (scenarios["Inefficient Developer"]["requests_per_day"] * 
             scenarios["Inefficient Developer"]["avg_input_tokens"] * 30 / 1_000_000) * prices["input"] +
            (scenarios["Inefficient Developer"]["requests_per_day"] * 
             scenarios["Inefficient Developer"]["avg_output_tokens"] * 30 / 1_000_000) * prices["output"]
        ) * 12
        
        efficient = (
            (scenarios["Efficient Developer"]["requests_per_day"] * 
             scenarios["Efficient Developer"]["avg_input_tokens"] * 30 / 1_000_000) * prices["input"] +
            (scenarios["Efficient Developer"]["requests_per_day"] * 
             scenarios["Efficient Developer"]["avg_output_tokens"] * 30 / 1_000_000) * prices["output"]
        ) * 12
        
        print(f"   {model:<20} ${inefficient - efficient:>7.2f}/year")
    
    print("\n💰 For a team of 10 developers:")
    team_savings = (
        (scenarios["Inefficient Developer"]["requests_per_day"] * 8000 * 30 / 1_000_000) * 10 -
        (scenarios["Efficient Developer"]["requests_per_day"] * 2000 * 30 / 1_000_000) * 10
    ) * 12
    print(f"   Potential savings: ${team_savings * 10:.2f}/year (using GPT-4 Turbo)")
    
    input("\nPress Enter to continue...")


# ============================================================================
# Main Demo Flow
# ============================================================================

def main():
    """Run all demos."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  Workshop 2: AI Token-Efficient Usage - Demo Script".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "═" * 68 + "╝")
    
    demos = [
        ("Token Counting Basics", demo_token_counting),
        ("Code Verbosity Impact", demo_code_verbosity),
        ("Prompt Efficiency", demo_prompt_efficiency),
        ("Incremental vs. Monolithic", demo_incremental_vs_monolithic),
        ("Context Loading", demo_context_efficiency),
        ("Agentic Token Costs", demo_agentic_costs),
        ("Cost Calculator", demo_cost_calculator),
    ]
    
    while True:
        print("\n" + "=" * 70)
        print("Demo Menu:")
        print("=" * 70)
        for i, (name, _) in enumerate(demos, 1):
            print(f"  {i}. {name}")
        print(f"  {len(demos) + 1}. Run all demos")
        print(f"  0. Exit")
        
        try:
            choice = input("\nSelect demo (0-{}): ".format(len(demos) + 1))
            choice = int(choice)
            
            if choice == 0:
                print("\n👋 Thanks for attending the workshop!")
                print("💡 Remember: Tokens = Money. Be efficient!\n")
                break
            elif choice == len(demos) + 1:
                for name, demo_func in demos:
                    demo_func()
            elif 1 <= choice <= len(demos):
                demos[choice - 1][1]()
            else:
                print("❌ Invalid choice. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break


if __name__ == "__main__":
    main()
