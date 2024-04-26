import cianparser

moscow_parser = cianparser.CianParser(location="Москва")


def main():
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(2,),
        with_saving_csv=True,
        additional_settings={
            "start_page": 1,
            "end_page": 50,
            "object_type": "secondary"
        })


if __name__ == '__main__':
    main()
