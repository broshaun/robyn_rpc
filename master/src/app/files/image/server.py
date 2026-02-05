import os
import config
from io import BytesIO
from PIL import Image


class ImgasS:
    def check_existing_file(self, name):
        os.makedirs(config.IMGS, exist_ok=True)
        return os.path.isfile(os.path.join(config.IMGS, name))

    def convert_to_jpg(
        self,
        file_content,
        quality=88,
        max_size=None,
        optimize=False,
        progressive=False,
        subsampling=2,
    ):
        """
        将图片二进制内容转换为 JPG（二进制）
        保持原始视觉方向，不发生旋转
        """
        try:
            with Image.open(BytesIO(file_content)) as img:
                # 处理透明图片：铺白底
                if img.mode in ("RGBA", "LA") or (
                    img.mode == "P" and "transparency" in img.info
                ):
                    img = img.convert("RGBA")
                    bg = Image.new("RGB", img.size, (255, 255, 255))
                    bg.paste(img, mask=img.getchannel("A"))
                    img = bg
                else:
                    img = img.convert("RGB")

                # 按最长边等比缩放
                if max_size:
                    img.thumbnail((max_size, max_size))

                buf = BytesIO()
                img.save(
                    buf,
                    format="JPEG",
                    quality=quality,
                    optimize=optimize,
                    progressive=progressive,
                    subsampling=subsampling,
                )
                return buf.getvalue()

        except Exception as e:
            raise ValueError(f"图片转换失败: {e}") from e