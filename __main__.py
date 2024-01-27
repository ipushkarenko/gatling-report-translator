from gtl_json_adapter import download_gtl_statistic

if __name__ == '__main__':
    dtos = download_gtl_statistic(".")
    df = (dtos)
    df
