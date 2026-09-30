@echo off
echo ========================================================
echo Generating Samsung PRISM Theme 04 PowerPoint File (.pptx)
echo ========================================================
echo.

python -c "import pptx" 2>NUL
if %errorlevel% neq 0 (
    echo Installing python-pptx library...
    pip install python-pptx
)

echo.
echo Running presentation generator...
python generate_theme04_ppt.py

echo.
echo ========================================================
echo SUCCESS! Samsung_PRISM_Theme04_Streaming_Live_RAG.pptx has been generated!
echo ========================================================
echo.
pause
