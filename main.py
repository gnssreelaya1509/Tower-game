import flet as ft
import threading
import time


def main(page: ft.Page):
    page.title = "Tower Builder Pro"
    page.theme_mode = "dark"
    page.bgcolor = "#0B0E14"

    # Game State
    game_state = {"is_running": True, "speed": 10, "current_height": 0}
    tower_stack = ft.Stack(height=500, width=400)

    # The moving block
    moving_block = ft.Container(width=150, height=30, bgcolor="#38BDF8", left=0, bottom=0)
    game_stack = ft.Container(content=tower_stack, bgcolor="#1E293B", width=400, height=500, border_radius=10)

    tower_stack.controls.append(moving_block)

    def animate_block():
        direction = 1
        while game_state["is_running"]:
            # Logic: move only the top-most block
            if moving_block.left >= 250 or moving_block.left <= 0:
                direction *= -1
            moving_block.left += (game_state["speed"] * direction)
            page.update()
            time.sleep(0.03)

    threading.Thread(target=animate_block, daemon=True).start()

    def drop_block(e=None):
        # 1. Lock the current block in place
        static_block = ft.Container(
            width=moving_block.width, height=30, bgcolor="#FBBF24",
            left=moving_block.left, bottom=game_state["current_height"]
        )
        tower_stack.controls.append(static_block)

        # 2. Reset moving block to the new level
        game_state["current_height"] += 30
        moving_block.bottom = game_state["current_height"]
        moving_block.left = 0

        # 3. Increase difficulty
        game_state["speed"] += 1
        page.update()

    page.on_keyboard_event = lambda e: drop_block() if e.key in ["Space", "Enter"] else None

    page.add(
        ft.Text("TOWER BUILDER: KEEP STACKING", size=24, weight="bold"),
        game_stack,
        ft.ElevatedButton("DROP (Space/Enter)", on_click=drop_block, bgcolor="#38BDF8")
    )


ft.app(target=main)