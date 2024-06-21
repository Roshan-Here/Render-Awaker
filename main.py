import asyncio
from Awaker.awaker import awaker_list
# from pathlib import Path
import os

# BASE_DIR = Path(__file__).resolve().parent.parent

# print(F"{BASE_DIR}/RENDER-AWAKER/siteslists.txt")

print("Running Script")


async def main():
    text_file_name = './siteslists.txt'
    await awaker_list(text_file_name)

if __name__ == "__main__":
    asyncio.run(main())