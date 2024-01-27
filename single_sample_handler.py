from typing import List
from _gtl_json_dto import GatlingStatsDto
import pandas as pd
import matplotlib.pyplot as plt


def _create_dataframe_from_dtos(dtos: List[GatlingStatsDto]) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from a list of GatlingStatsDto objects.

    :param dtos: List of GatlingStatsDto DTOs.
    :return: pandas DataFrame with the extracted data.
    """

    data = []
    for dto in dtos:
        for name, req in dto.contents.items():
            data.append({
                "Name": req.name,
                "Total requests": req.stats['numberOfRequests']['total'],
                "OK": req.stats['numberOfRequests']['ok'],
                "KO": req.stats['numberOfRequests']['ko'],
                "MRT[ms]": req.stats['meanResponseTime']['total']
            })

    return pd.DataFrame(data)


def parse_gtl_statistics(dtos: List[GatlingStatsDto]) -> pd.DataFrame:
    return _create_dataframe_from_dtos(dtos)


def print_result_table_by_name(df, filter_name) -> pd.DataFrame:
    """
        Filters the DataFrame for a given name, sorts by 'Total requests', adds a sequential index starting from 1,
        and prints the entire DataFrame with the new index.

        :param df: pandas DataFrame containing the data.
        :param filter_name: String to filter the DataFrame for a specific name.
        """
    # Filter and sort the DataFrame
    filtered_sorted_df = df[df['Name'].str.contains(filter_name)].sort_values(by='Total requests', ascending=True)

    # Reset index to get a new sequential index and drop the old index
    filtered_sorted_df = filtered_sorted_df.reset_index(drop=True)

    # Add a new column with a sequential number starting from 1
    filtered_sorted_df.index = range(1, len(filtered_sorted_df) + 1)

    # To print the entire DataFrame without truncation
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        return filtered_sorted_df


def plot_ok_vs_mrt(df, name_filter, title):
    """
    Plots OK and KO requests vs MRT for a specific name filter in the DataFrame.

    :param df: pandas DataFrame containing the data.
    :param name_filter: String to filter the DataFrame for a specific name.
    :param title: Title for the plot.
    """
    # Filter the DataFrame based on the name filter
    filtered_df = df[df['Name'].str.contains(name_filter)].sort_values(by='Total requests', ascending=True)

    plt.figure(figsize=(9, 5))

    # Plot OK Requests vs MRT[ms] as a line in blue
    plt.plot(filtered_df['Total requests'], filtered_df['MRT[ms]'], color='blue', label='OK Requests', linestyle='-', marker='o')

    plt.title(f'{title}')
    plt.xlabel('Number Of Concurrent Requests [per sec]')
    plt.ylabel('MRT[ms]')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_ok_ko_vs_total_requests(df, name_filter, title):
    """
       Plots OK and KO requests in relation to total number of requests for a specific name filter in the DataFrame,
       using lines instead of points.

       :param df: pandas DataFrame containing the data.
       :param name_filter: String to filter the DataFrame for a specific name.
       :param title: Title for the plot.
       """
    # Filter the DataFrame based on the name filter
    filtered_df = df[df['Name'].str.contains(name_filter)].sort_values(by='Total requests', ascending=True).copy()

    # Calculate the total number of requests
    filtered_df['Total'] = filtered_df['OK'] + filtered_df['KO']

    # Create the plot
    plt.figure(figsize=(9, 5))

    # Plot OK Requests vs Total Requests as lines in blue
    plt.plot(filtered_df['Total'], filtered_df['OK'], color='blue', label='OK Requests', linestyle='-', marker='o')

    # Plot KO Requests vs Total Requests as lines in red
    plt.plot(filtered_df['Total'], filtered_df['KO'], color='red', label='KO Requests', linestyle='-', marker='o')

    plt.title(f'{title}')
    plt.xlabel('Total Number of Requests')
    plt.ylabel('Number of OK/KO Requests')
    plt.legend()
    plt.grid(True)
    plt.show()
