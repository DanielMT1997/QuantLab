import pandas as pd


def calculate_strategy_returns(
    returns: pd.Series,
    position: pd.Series
) -> pd.Series:
    """
    Calculate strategy returns from asset returns and strategy position.

    Parameters
    ----------
    returns : pd.Series
        Asset daily returns.
    position : pd.Series
        Strategy position. For example:
        1 means fully invested,
        0 means out of the market,
        -1 means short.

    Returns
    -------
    pd.Series
        Strategy daily returns.
    """
    strategy_returns = position.shift(1) * returns
    strategy_returns = strategy_returns.dropna()

    return strategy_returns


def calculate_equity_curve(
    strategy_returns: pd.Series
) -> pd.Series:
    """
    Calculate equity curve from strategy returns.

    Parameters
    ----------
    strategy_returns : pd.Series
        Strategy daily returns.

    Returns
    -------
    pd.Series
        Equity curve normalized to 1 at the beginning.
    """
    equity_curve = (1 + strategy_returns).cumprod()

    return equity_curve


def run_backtest(
    returns: pd.Series,
    position: pd.Series
) -> tuple[pd.Series, pd.Series]:
    """
    Run a simple backtest from asset returns and strategy position.

    Parameters
    ----------
    returns : pd.Series
        Asset daily returns.
    position : pd.Series
        Strategy position.

    Returns
    -------
    tuple[pd.Series, pd.Series]
        Strategy returns and equity curve.
    """
    validate_inputs(returns, position)
    strategy_returns = calculate_strategy_returns(returns, position)
    equity_curve = calculate_equity_curve(strategy_returns)

    return strategy_returns, equity_curve


def compare_equity_curves(
        equity_curves: dict[str, pd.Series]
) -> pd.DataFrame:
    """
    Compares several equity curves and returns a datafreme ready to graph and compare.

    Parameters
    -----------
    equity_curves : dict[str, pd.Series]
        Equity curves.

    Returns
    -------
    pd.DataFrame
    """
    comparison = pd.DataFrame(equity_curves).dropna() #dropna para quitar los posibles días en los que haya alguna curva sin datos.
    return comparison

def validate_inputs(returns: pd.Series, position: pd.Series) -> None:
    """
    Checks if returns and position are actually compatible to execute a backtest.

    Parameters
    -----------
    returns : the returns of an equity

    position : the position of a strategy
    """
    if not isinstance(returns, pd.Series):
        raise TypeError("returns must be a pandas Series")
    if not isinstance(position, pd.Series):
        raise TypeError("position must be a pandas Series")
    if not returns.index.equals(position.index):
        raise ValueError("returns and positions have different indices")
    if returns.isnull().values.any():
        raise ValueError("There are missing values in the returns")
    if position.isnull().values.any():
        raise ValueError("There are missing values in the position")
