import pytest
import pandas as pd
from project import prepare_dataframe, calculate_relative_performance

def test_prepare_dataframe():
    tickers = ['AAPL', 'GOOGL']
    df = prepare_dataframe(tickers)
    assert df is not None, "Dataframe should not be None"
    assert not df.empty, "Dataframe should not be empty"
    assert set(df.columns) == set(tickers), "Dataframe should have the specified tickers as columns"

def test_calculate_relative_performance():
    data = {
        'AAPL': [100, 200, 300],
        'GOOGL': [500, 600, 700]
    }
    df = pd.DataFrame(data)
    relative_performance = calculate_relative_performance(df)

    expected_data = {
        'AAPL': [1.0, 2.0, 3.0],
        'GOOGL': [1.0, 1.2, 1.4]
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(relative_performance, expected_df, check_dtype=False)
