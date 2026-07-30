import requests
from bs4 import BeautifulSoup


def decode_secret_message(url: str) -> None:
    """Takes a Google Doc URL containing 2D character coordinates, parses the

    table, and prints the secret message graphic correctly oriented.
    """
    # 1. Retrieve published web page content
    response = requests.get(url)
    response.raise_for_status()

    # 2. Extract table rows from HTML
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        print("Error: Could not find a data table in the provided document.")
        return

    grid_data = []

    # Parse rows (skip header row)
    for row in table.find_all("tr")[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) < 3:
            continue

        col0 = cells[0].text.strip()
        char = cells[1].text.strip()
        col2 = cells[2].text.strip()

        try:
            x = int(col0)
            y = int(col2)
            grid_data.append((x, y, char))
        except ValueError:
            continue

    if not grid_data:
        print("No valid character data found.")
        return

    # 3. Compute dynamic dimensions
    max_x = max(pt[0] for pt in grid_data)
    max_y = max(pt[1] for pt in grid_data)

    # 4. Construct character grid pre-filled with space characters
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # 5. Populate grid with y-coordinate inverted (y=0 mapped to bottom row)
    for x, y, char in grid_data:
        grid[max_y - y][x] = char

    # 6. Print the graphic to stdout
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    decode_secret_message(doc_url)
