import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Add stocks table to keep track of the stocks owned by each user
db.execute("DROP TABLE stocks")
db.execute("CREATE TABLE stocks (id INTEGER AUTO_INCREMENT, user_id INTEGER NOT NULL, symbol TEXT NOT NULL, stockname TEXT NOT NULL, shares NUMERIC NOT NULL, price REAL NOT NULL, total REAL NOT NULL, date DATETIME NOT NULL, PRIMARY KEY (id) FOREIGN KEY (user_id) REFERENCES users (id))")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    
    # Get the user's current cash balance and stocks
    rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = rows[0]["cash"]
    stocks = db.execute("SELECT symbol, stockname, shares, price, total FROM stocks WHERE user_id = ?", session["user_id"])
    unique_stocks = {}

        
    if len(stocks) == 0:
        total = cash
        return render_template("index.html", cash=cash, stocks=stocks, total=total)

    for stock in stocks:
        if stock["symbol"] not in unique_stocks:
            unique_stocks[stock["symbol"]] = {"stockname": stock["stockname"], "shares": stock["shares"], "price": stock["price"], "total": stock["total"]}
        else:
            unique_stocks[stock["symbol"]]["shares"] += stock["shares"]
            unique_stocks[stock["symbol"]]["total"] += stock["total"]
    
    for stock in unique_stocks:
        unique_stocks[stock]["price"] = lookup(stock)["price"]
        unique_stocks[stock]["total"] = unique_stocks[stock]["shares"] * unique_stocks[stock]["price"]
        total = cash + unique_stocks[stock]["total"]
    
    # for stock in unique_stocks:
    #     print(stock)
    #     print(unique_stocks[stock]["stockname"])
    #     print(unique_stocks[stock]["shares"])
    #     print(unique_stocks[stock]["price"])
    #     print(unique_stocks[stock]["total"])


    return render_template("index.html", cash=cash, stocks=unique_stocks, total=total)

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        else:
            quote = lookup(request.form.get("symbol"))
            if quote == None:
                return apology("invalid symbol", 400)
            else:
                return render_template("quoted.html", name=quote["name"], price=quote["price"], symbol=quote["symbol"])
    else:
        return render_template("quote.html")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        elif not request.form.get("shares"):
            return apology("must provide shares", 400)
        else:
            quote = lookup(request.form.get("symbol"))
            if quote == None:
                return apology("invalid symbol", 400)
            else:
                # print("QUOTE: ", quote)
                # print("QUOTE SYMBOL: ", quote["symbol"])
                # print("QUOTE NAME: ", quote["name"])
                # print("QUOTE PRICE: ", quote["price"])
                # print("Shares: ", request.form.get("shares"))

                rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                cash = rows[0]["cash"]
                price = quote["price"]
                shares = int(request.form.get("shares"))
                total = price * shares
                if total > cash:
                    return apology("insufficient funds", 400)
                else:
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total, session["user_id"])
                    db.execute("INSERT INTO stocks (user_id, symbol, stockname, shares, price, total, date) VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)", session["user_id"], quote["symbol"], quote["name"], shares, price, total)
                    return redirect("/")    
    else:
        return render_template("buy.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        elif not request.form.get("shares"):
            return apology("must provide shares", 400)
        else:
            quote = lookup(request.form.get("symbol"))
            if quote == None:
                return apology("invalid symbol", 400)
            else:
                # print("QUOTE: ", quote)
                # print("QUOTE SYMBOL: ", quote["symbol"])
                # print("QUOTE NAME: ", quote["name"])
                # print("QUOTE PRICE: ", quote["price"])
                # print("Shares: ", request.form.get("shares"))
                
                rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                cash = rows[0]["cash"]
                price = quote["price"]
                shares = int(request.form.get("shares"))
                total = price * shares
                db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + total, session["user_id"])
                db.execute("INSERT INTO stocks (user_id, symbol, stockname, shares, price, total, date) VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)", session["user_id"], quote["symbol"], quote["name"], -shares, price, -total)
                return redirect("/")    
    else:
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]
        stocks = db.execute("SELECT symbol, stockname, shares, price, total FROM stocks WHERE user_id = ?", session["user_id"])
        unique_stocks = {}

        for stock in stocks:
            if stock["symbol"] not in unique_stocks:
                unique_stocks[stock["symbol"]] = {"stockname": stock["stockname"], "shares": stock["shares"], "price": stock["price"], "total": stock["total"]}
            else:
                unique_stocks[stock["symbol"]]["shares"] += stock["shares"]
                unique_stocks[stock["symbol"]]["total"] += stock["total"]
        
        for stock in unique_stocks:
            unique_stocks[stock]["price"] = lookup(stock)["price"]
            unique_stocks[stock]["total"] = unique_stocks[stock]["shares"] * unique_stocks[stock]["price"]
            total = cash + unique_stocks[stock]["total"]
        
        unique_symbols = []
        for stock in unique_stocks:
            unique_symbols.append(stock)

        return render_template("sell.html", stocks=unique_symbols)

@app.route("/refill", methods=["POST"])
@login_required
def refill():
    """Refill cash"""
    if request.method == "POST":
        if not request.form.get("refill"):
            return apology("must provide cash", 400)
        else:
            cash = float(request.form.get("refill"))
            rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + rows[0]["cash"], session["user_id"])
            return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stocks = db.execute("SELECT symbol, stockname, shares, price, total, date FROM stocks WHERE user_id = ?", session["user_id"])
    return render_template("history.html", stocks=stocks)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)
        else:
            rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
            if len(rows) == 1:
                return apology("username already exists", 403)
            else:
                db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password")))
                return redirect("/")
    else:
        return render_template("register.html")

