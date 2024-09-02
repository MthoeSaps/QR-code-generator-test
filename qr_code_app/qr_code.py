import streamlit as st
import qrcode
import io

# Streamlit app title
st.title("Personalized QR Code Generator")

# Input fields for personal data
name = st.text_input("Enter your name (optional):")
email = st.text_input("Enter your email (optional):")
phone = st.text_input("Enter your phone number (optional):")

# Text area for additional input
input_text = st.text_area("Enter text or URL to generate QR code (optional):")

if st.button("Generate QR Code"):
    # Check if at least one field is filled
    if input_text or name or email or phone:
        # Combine all inputs into a single string
        combined_data = ""
        if name:
            combined_data += f"Name: {name}\n"
        if email:
            combined_data += f"Email: {email}\n"
        if phone:
            combined_data += f"Phone: {phone}\n"
        if input_text:
            combined_data += f"Input: {input_text}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(combined_data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a BytesIO object
        buf = io.BytesIO()
        img.save(buf, format='PNG')  # Save as PNG to the buffer
        buf.seek(0)

        # Display the QR code image using the buffer
        st.image(buf, caption="Generated QR Code", use_column_width=True)  # Use the buffer directly

        # Download link for the QR code
        st.download_button(
            label="Download QR Code",
            data=buf.getvalue(),  # Get the bytes from the buffer
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Please fill in at least one field.")
