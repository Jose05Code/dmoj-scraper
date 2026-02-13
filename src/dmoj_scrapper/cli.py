from .login import login
from .scrapping import scrapping_problems, main_scrapping
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="DMOJ Scraper - Download your DMOJ submissions",
        epilog="Example: %(prog)s -u jose05code"
    )

    parser.add_argument(
        '-u', '--user',
        required=False,
        help='User for login'
    )

    parser.add_argument(
        '-p', '--password',
        required=False,
        help='Password to use when connecting to server'
    )

    args = parser.parse_args()


    # Handle case with arguments and interactive cli case
    if (args.user and args.password):
        user_session = login(args.user, args.password)
    else:
        user_session = login()

    if user_session:
        problem_list = scrapping_problems(user_session)
        main_scrapping(user_session, problem_list)



if __name__ == '__main__':
    main()
