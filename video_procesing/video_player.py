import cv2

def play_video(video_title):
    video_path = f"../video_out/{video_title}/final/{video_title}.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: cant open video")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video Playback', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
