import numpy as np
import pandas as pd


def total_return(equity_curve: pd.Series) -> float:
    """
    Calculate total return from an equity curve.

    Parameters
    ----------
    equity_curve : pd.Series
        Equity curve representing the value of the strategy through time.
        It is usually normalized to 1, but the function also works if it
        starts from another initial capital.

    Returns
    -------
    float
        Total return over the full period.
    """
    return equity_curve.iloc[-1] / equity_curve.iloc[0] - 1


def annualized_return(equity_curve: pd.Series) -> float:
    """
    Calculate annualized compound return from an equity curve.

    Parameters
    ----------
    equity_curve : pd.Series
        Equity curve indexed by dates.

    Returns
    -------
    float
        Annualized compound return.
    """
    start_date = equity_curve.index[0]
    end_date = equity_curve.index[-1]
    years = (end_date - start_date).days / 365.25

    total_growth = equity_curve.iloc[-1] / equity_curve.iloc[0]

    return total_growth ** (1 / years) - 1


def annualized_volatility(
    returns: pd.Series,
    trading_days: int = 252
) -> float:
    """
    Calculate annualized volatility from daily returns.

    Parameters
    ----------
    returns : pd.Series
        Daily returns of the asset or strategy.
    trading_days : int
        Number of trading days per year. By default, 252.

    Returns
    -------
    float
        Annualized volatility.
    """
    return returns.std() * np.sqrt(trading_days)


def drawdown(equity_curve: pd.Series) -> pd.Series:
    """
    Calculate the drawdown series from an equity curve.

    Parameters
    ----------
    equity_curve : pd.Series
        Equity curve representing the value of the strategy through time.

    Returns
    -------
    pd.Series
        Drawdown series. Values are expressed as negative percentages
        relative to the previous running maximum.
    """
    running_max = equity_curve.cummax()
    return equity_curve / running_max - 1


def max_drawdown(equity_curve: pd.Series) -> float:
    """
    Calculate the maximum drawdown from an equity curve.

    Parameters
    ----------
    equity_curve : pd.Series
        Equity curve representing the value of the strategy through time.

    Returns
    -------
    float
        Maximum drawdown over the full period.
    """
    return drawdown(equity_curve).min()


def performance_summary(
    equity_curve: pd.Series,
    returns: pd.Series
) -> pd.Series:
    """
    Create a summary of the main performance and risk metrics.

    Parameters
    ----------
    equity_curve : pd.Series
        Equity curve of the strategy.
    returns : pd.Series
        Periodic returns of the strategy.

    Returns
    -------
    pd.Series
        Summary containing total return, annualized return,
        annualized volatility and maximum drawdown.
    """
    return pd.Series({
        "Rentabilidad total": total_return(equity_curve),
        "Rentabilidad anualizada": annualized_return(equity_curve),
        "Volatilidad anualizada": annualized_volatility(returns),
        "Máximo drawdown": max_drawdown(equity_curve),
    })