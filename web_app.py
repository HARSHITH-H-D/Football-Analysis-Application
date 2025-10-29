import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw

# Constants
pitch_width = 1300
pitch_height = 900

# Formation coordinates (left side by default)
formations = {
    '4-3-3': [(225, 150), (225, 350), (225, 550), (225, 750),
              (350, 200), (350, 450), (350, 700),
              (480, 200), (480, 450), (480, 700)],
    '4-4-2': [(225, 150), (225, 350), (225, 550), (225, 750),
              (350, 150), (350, 350), (350, 550), (350, 750),
              (480, 300), (480, 600)],
    '3-4-3': [(225, 250), (225, 450), (225, 650),
              (350, 150), (350, 350), (350, 550), (350, 750),
              (480, 200), (480, 450), (480, 700)]
}

formation_positions = {
    '4-3-3': ['LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'CM', 'LW', 'ST', 'RW'],
    '4-4-2': ['LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'ST', 'ST'],
    '3-4-3': ['CB', 'CB', 'CB', 'LM', 'CM', 'CM', 'RM', 'LW', 'ST', 'RW']
}

# Draw the football pitch
def draw_pitch_background():
    pitch = Image.new('RGB', (pitch_width, pitch_height), (34, 139, 34))  # Green
    draw = ImageDraw.Draw(pitch)
    draw.rectangle([0, 0, pitch_width, pitch_height], outline="white", width=5)
    draw.line([(pitch_width//2, 0), (pitch_width//2, pitch_height)], fill="white", width=5)
    center = (pitch_width//2, pitch_height//2)
    r = 90
    draw.ellipse([center[0]-r, center[1]-r, center[0]+r, center[1]+r], outline="white", width=5)
    draw.rectangle([0, 225, 165, 675], outline="white", width=5)
    draw.rectangle([0, 360, 55, 540], outline="white", width=5)
    draw.rectangle([pitch_width-165, 225, pitch_width, 675], outline="white", width=5)
    draw.rectangle([pitch_width-55, 360, pitch_width, 540], outline="white", width=5)
    draw.ellipse([100-5, pitch_height//2-5, 100+5, pitch_height//2+5], fill="white")
    draw.ellipse([pitch_width-100-5, pitch_height//2-5, pitch_width-100+5, pitch_height//2+5], fill="white")
    draw.ellipse([pitch_width//2-5, pitch_height//2-5, pitch_width//2+5, pitch_height//2+5], fill="white")
    return pitch

# Main App
def app():
    
    st.title("⚽ Football Tactics Board")

    col1, col2 = st.columns(2)
    with col1:
        team1_form = st.selectbox("Select Team 1 Formation", list(formations.keys()), key="team1")
    with col2:
        team2_form = st.selectbox("Select Team 2 Formation", list(formations.keys()), key="team2")

    # Background image
    bg_image = draw_pitch_background()

    # Session state for persistence
    if "formation_key" not in st.session_state:
        st.session_state.formation_key = 0
    if "objects" not in st.session_state:
        st.session_state.objects = []

    # Generate formation
    if st.button("Generate Formation"):
        st.session_state.formation_key += 1
        objects = []

        # Goalkeepers
        objects.extend([
            {"type": "circle", "left": 80, "top": pitch_height//2 - 25, "radius": 25, "fill": "yellow"},
            {"type": "text", "left": 80, "top": pitch_height//2 - 25, "text": "GK", "fill": "black", "fontSize": 16},
            {"type": "circle", "left": pitch_width - 130, "top": pitch_height//2 - 25, "radius": 25, "fill": "yellow"},
            {"type": "text", "left": pitch_width - 130, "top": pitch_height//2 - 25, "text": "GK", "fill": "black", "fontSize": 16}
        ])

        # Team 1 players (left side)
        for idx, (x, y) in enumerate(formations[team1_form]):
            if 0 <= x <= pitch_width and 0 <= y <= pitch_height:
                pos = formation_positions[team1_form][idx]
                objects.extend([
                    {"type": "circle", "left": x, "top": y, "radius": 20, "fill": "blue"},
                    {"type": "text", "left": x, "top": y, "text": pos, "fill": "white", "fontSize": 16}
                ])
            else:
                st.write(f"Team 1 player {pos} out of bounds at ({x}, {y})")

        # Team 2 players (right side, mirrored)
        for idx, (x, y) in enumerate(formations[team2_form]):
            mirrored_x = pitch_width - x
            if 0 <= mirrored_x <= pitch_width and 0 <= y <= pitch_height:
                pos = formation_positions[team2_form][idx]
                objects.extend([
                    {"type": "circle", "left": mirrored_x, "top": y, "radius": 20, "fill": "red"},
                    {"type": "text", "left": mirrored_x, "top": y, "text": pos, "fill": "white", "fontSize": 16}
                ])
            else:
                st.write(f"Team 2 player {pos} out of bounds at ({mirrored_x}, {y})")

        # Ball
        objects.append({
            "type": "circle", "left": pitch_width//2, "top": pitch_height//2, "radius": 15, "fill": "white"
        })

        st.session_state.objects = objects
        st.write(f"Generated {len(objects)} objects.")

    # Render canvas
    canvas_key = f"canvas_{st.session_state.formation_key}"
    st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=5,
        background_image=bg_image,
        height=pitch_height,
        width=pitch_width,
        drawing_mode="transform",
        initial_drawing={"version": "4.4.0", "objects": st.session_state.objects},
        key=canvas_key
    )

# Main entry
if __name__ == "__main__":
    app()
