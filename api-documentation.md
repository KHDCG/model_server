# ViT inference API

<a href="http://cataractmodel.hunian.site/docs">Go to Swagger UI</a>

## Endpoint

```
POST /inference
```

## Request

- Method : POST
- Content-Type : application/json

Request Body Example (JSON):

```
{
  "img": "base64_encoded_image_string",
}
```

| parameter	| Type	| Description |
| --- | --- | --- |
| img | string | Base64로 인코딩된 이미지 문자열 |

## Response

- Status Code : 200 OK
- Content-Type : application/json

Response Body Example (JSON):

```
{
  "predicted_class": "incipient",
  "probability": 0.85,
  "all_probability": [0.85, 0.1, 0.03, 0.02],
  "lime": "LIME image data (Base64-encoded)",
  "grad_cam": "Grad CAM encoding data (Base64-encoded)"
}
```

| Field	| Type | Description |
| --- | --- | --- |
| predicted_class |	string | 예측된 클래스 레이블 |
| probability | float | 예측된 클래스의 확률 값 |
| all_probability	| list | 모든 클래스에 대한 확률 목록 |
| lime | string | LIME 이미지 (Base64) |
| grad_cam | string | Grad CAM 이미지 (Base64) |