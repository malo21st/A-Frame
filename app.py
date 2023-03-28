import streamlit as st
import streamlit.components.v1 as components

html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>MDN Games: A-Frame demo</title>
  <script src="aframe.min.js"></script>
</head>
<body>
  <!-- HTML goes here -->
  <a-scene>
      <a-sky color="#DDDDDD"></a-sky>
      <a-box
          color="#0095DD"
          position="0 1 0"
          rotation="20 40 0">
      </a-box>
  </a-scene>
</body>
</html>
"""

components.html(html, height=720)
