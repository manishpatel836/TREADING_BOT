import typer
import questionary
from bot.client import get_client
from bot.loging_config import loggings
from bot.validators import symbol_validation,price_validation,quantity_validation
from bot.orders import place_limit_order,place_market_order
loggings()

app = typer.Typer(help='TRADING BOT')
@app.command()
def trade():
    typer.clear()
    typer.secho('Please Enter the details')
    try:
        client = get_client()
        typer.secho('Client is ready! Please enter the following details carefully:', fg=typer.colors.BRIGHT_YELLOW)
    except Exception:
        typer.secho("Failed to initialize client. Check bot.log.", fg=typer.colors.RED)
        raise typer.Exit(1)
    symbol_txt = typer.style("Enter trading symbol (BTCUSDT)", fg=typer.colors.BRIGHT_GREEN, bold=True)    
    symbol = typer.prompt(symbol_txt,str)
    symbol = symbol_validation(symbol)
    side = questionary.select(
        "BUY or SELL?",
        choices=["BUY", "SELL"],
        style=questionary.Style([('highlighted', 'fg:ansiyellow bold')])
    ).ask()
    type = questionary.select(
        "MARKET or LIMIT?",
        choices=["MARKET", "LIMIT"],
        style=questionary.Style([('highlighted', 'fg:ansiyellow bold')])
    ).ask()
    
    qty_text = typer.style("Enter quantity to trade", fg=typer.colors.BRIGHT_CYAN, bold=True)
    quantity = typer.prompt(qty_text, type=float)
    quantity = quantity_validation(quantity)
    price = None
    if type == 'LIMIT':
        price_text = typer.style("Enter the LIMIT price", fg=typer.colors.BRIGHT_GREEN, bold=True)
        price = typer.prompt(price_text, type=float)
        price = price_validation(price=price)
        place_limit_order(client=client,symbol=symbol,quantity=quantity,price=price,type=type,side=side)
    else:
        place_market_order(client=client,symbol=symbol,quantity=quantity,type=type,side=side)

if __name__ =='__main__':
    app()