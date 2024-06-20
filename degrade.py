print("by sofiaiaia rs")
def hex_to_custom_format(hex_color, text_char, bold):
    hex_color = hex_color.lstrip('#')
    custom_format = ""
    if text_char != ' ':
        custom_format = "&x"
        for char in hex_color:
            custom_format += f"&{char.lower()}"
    if bold and text_char != ' ':
        custom_format += "&l"
    custom_format += f"{text_char}"
    return custom_format
def create_gradient(start_color, end_color, text, max_length=245):
    start_color = start_color.lstrip('#')
    end_color = end_color.lstrip('#')
    formatted_strings = []
    while True:
        steps = len(text)
        start_rgb = tuple(int(start_color[i:i+2], 16) for i in (0, 2, 4))
        end_rgb = tuple(int(end_color[i:i+2], 16) for i in (0, 2, 4))
        delta_r = (end_rgb[0] - start_rgb[0]) / steps
        delta_g = (end_rgb[1] - start_rgb[1]) / steps
        delta_b = (end_rgb[2] - start_rgb[2]) / steps
        gradient_colors = []
        for step in range(steps):
            r = int(start_rgb[0] + delta_r * step)
            g = int(start_rgb[1] + delta_g * step)
            b = int(start_rgb[2] + delta_b * step)
            hex_color = f"{r:02x}{g:02x}{b:02x}"
            gradient_colors.append(hex_color)
        formatted_strings = []
        for i, hex_color in enumerate(gradient_colors):
            formatted_string = hex_to_custom_format(hex_color, text[i], bold)
            formatted_strings.append(formatted_string)
        final_output = "".join(formatted_strings)
        if len(final_output) <= max_length:
            break
        text = text[:-1]
    return final_output
if __name__ == "__main__":
    hex_color1 = input("Digite o primeiro código hexadecimal (com ou sem #): ").strip()
    hex_color2 = input("Digite o segundo código hexadecimal (com ou sem #): ").strip()
    text = input("Texto a ser adicionado após o formato: ").strip()
    answer = input("Negrito? (s/n): ").strip().lower()
    bold = answer == 's'
    result = create_gradient(hex_color1, hex_color2, text)
    print(result)
