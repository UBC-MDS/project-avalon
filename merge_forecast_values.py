def merge_forecast_values(original_df, forecasted_values, col_name):

    index_freq = original_df.index.inferred_freq
    next_date = pd.Timestamp(original_df.index[-1]) + pd.tseries.frequencies.to_offset(index_freq)
    
    forecasted_dates = original_df.index[len(original_df) - len(forecasted_values) + 1:]
    forecasted_dates = forecasted_dates.append(pd.DatetimeIndex([next_date]))

    forecasted_df = pd.DataFrame({col_name: forecasted_values}, index=forecasted_dates)

    merged_df = pd.concat([original_df, forecasted_df], axis=1)
    return merged_df