import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

blur_faces = True  

with mp_fd.FaceDetection(model_selection=0, min_detection_confidence=0.6) as fd:
    while True:
        ok, frame = cap.read()
        if not ok: break

        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = fd.process(rgb)

        out = frame.copy()

        if res.detections:
            for det in res.detections:
                box = det.location_data.relative_bounding_box
                x1 = int(box.xmin * w); y1 = int(box.ymin * h)
                bw = int(box.width * w); bh = int(box.height * h)
                x2, y2 = x1 + bw, y1 + bh

                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(w, x2), min(h, y2)

                if blur_faces:
                    roi = out[y1:y2, x1:x2]
                    if roi.size:
                        roi = cv2.GaussianBlur(roi, (31, 31), 0)
                        out[y1:y2, x1:x2] = roi

                cv2.rectangle(out, (x1, y1), (x2, y2), (0,255,0), 2)

        cv2.putText(out, "Face detection: q quit | b toggle blur",
                    (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

        cv2.imshow("Face Detection", out)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"): break
        if key == ord("b"): blur_faces = not blur_faces

cap.release()
cv2.destroyAllWindows()