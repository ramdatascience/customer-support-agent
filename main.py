from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from agents.support_agent import SupportAgent

load_dotenv()
console = Console()


def print_banner():
    console.print(Panel(
        Text("🤖 TechCorp Customer Support Agent", justify="center", style="bold cyan"),
        subtitle="Powered by LangChain + OpenAI",
        border_style="cyan",
    ))
    console.print("[dim]Type 'exit' or 'quit' to end the session.[/dim]\n")


def main():
    print_banner()
    agent = SupportAgent()

    while True:
        try:
            user_input = console.input("[bold green]You:[/bold green] ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                console.print("\n[bold cyan]Agent:[/bold cyan] Thank you for contacting TechCorp support. Goodbye! 👋")
                break

            console.print()
            response = agent.chat(user_input)
            console.print(Panel(response, title="[bold cyan]Agent[/bold cyan]", border_style="blue"))
            console.print()

        except KeyboardInterrupt:
            console.print("\n[yellow]Session interrupted.[/yellow]")
            break


if __name__ == "__main__":
    main()