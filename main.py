import asyncio
from Awaker.awaker import awaker_list

async def main():
    text_file_name = './siteslists.txt'
    await awaker_list(text_file_name)

if __name__ == "__main__":
    asyncio.run(main())