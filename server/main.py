from mcp.server.fastmcp import FastMCP

mcp = FastMCP("haiguitang")

@mcp.tool()
async def ask_question(question: str) -> str:
    """提交一个是非问题"""
    return f"收到问题：{question}（骨架，待接后端）"

@mcp.tool()
async def get_hint() -> str:
    """获取一条提示"""
    return "这是骨架提示"

@mcp.tool()
async def submit_guess(guess: str) -> str:
    """提交你的推理"""
    return f"收到推理：{guess}（骨架，待评分）"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
