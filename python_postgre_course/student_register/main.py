from app import App


if __name__ == "__main__":
    try:
        application = App()
        application.run()
    except Exception as e:
        print(e)