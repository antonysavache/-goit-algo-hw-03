import os
import sys
import shutil
from pathlib import Path

def sort_files(source_dir: str, dest_dir: str = 'dist') -> None:
    try:
        source_path = Path(source_dir)
        dest_path = Path(dest_dir)

        dest_path.mkdir(exist_ok=True)

        def process_directory(current_path: Path) -> None:
            try:
                for item in current_path.iterdir():
                    try:
                        if item.is_file():
                            extension = item.suffix[1:].lower() if item.suffix else 'no_extension'
                            extension_dir = dest_path / extension
                            extension_dir.mkdir(exist_ok=True)
                            shutil.copy2(item, extension_dir / item.name)
                            print(f"Скопирован файл: {item.name} -> {extension_dir}")

                        elif item.is_dir():
                            process_directory(item)

                    except PermissionError:
                        print(f"Ошибка доступа к файлу/директории: {item}")
                    except Exception as e:
                        print(f"Ошибка при обработке {item}: {str(e)}")

            except PermissionError:
                print(f"Ошибка доступа к директории: {current_path}")
            except Exception as e:
                print(f"Ошибка при обработке директории {current_path}: {str(e)}")

        process_directory(source_path)
        print(f"\nСортировка завершена. Файлы перемещены в директорию: {dest_path}")

    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Использование: python script.py source_dir [dest_dir]")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    if not os.path.exists(source_dir):
        print(f"Ошибка: Исходная директория '{source_dir}' не существует")
        sys.exit(1)

    sort_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()