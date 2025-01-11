import cv2

def overlay_text_with_background(img, content, coords, font_style, scale, thickness, text_color, background_color, alpha, padding=10):
    temp_image = img.copy()
    text_dimensions, baseline = cv2.getTextSize(content, font_style, scale, thickness)
    text_w, text_h = text_dimensions

    box_start_x = coords[0] - padding
    box_start_y = coords[1] - text_h - padding
    box_end_x = coords[0] + text_w + padding
    box_end_y = coords[1] + baseline + padding

    cv2.rectangle(temp_image, (box_start_x, box_start_y), (box_end_x, box_end_y), background_color, -1)
    cv2.addWeighted(temp_image, alpha, img, 1 - alpha, 0, img)

    cv2.putText(img, content, coords, font_style, scale, text_color, thickness)

def create_rectangle(img, corner1, corner2, rect_color, line_thickness):
    cv2.rectangle(img, corner1, corner2, rect_color, line_thickness)

img = cv2.imread('assignment-001-given.jpg')

overlay_text = 'RAH972U'
font_type = cv2.FONT_HERSHEY_SIMPLEX
font_size = 2
font_thick = 5
txt_color = (0, 255, 0)
box_color = (0, 0, 0)
transparency = 0.5
padding_space = 120

img_h, img_w, _ = img.shape
text_dims, _ = cv2.getTextSize(overlay_text, font_type, font_size, font_thick)
text_w, text_h = text_dims
text_pos_x = img_w - text_w - padding_space
text_pos_y = text_h + padding_space

overlay_text_with_background(img, overlay_text, (text_pos_x, text_pos_y), font_type, font_size, font_thick, txt_color, box_color, transparency)
create_rectangle(img, (200, 200), (950, 950), (0, 255, 0), 10)

cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.imwrite('assignment-001-result.jpg', img)
cv2.destroyAllWindows()