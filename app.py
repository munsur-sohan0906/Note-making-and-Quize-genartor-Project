import streamlit as st
from api_calling import note_generator,audio_transcript,quiz_generator
from PIL import Image


#title
st.title("Note Summary And Quiz Generator")
st.markdown("Upload 3 image to genarate note summary and genearte Quiz")
st.divider()

#sidebar
with st.sidebar:
    #image
    images=st.file_uploader("Upload yours Note Photo",
                            type=['jpg','png','jpeg'],
                            accept_multiple_files=True)
    
    #convert pil images
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload only 3 images")
        else:
            # st.image(image)
            col=st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img) 

    #catagory
    option=st.selectbox(
        "Enter the Difficulty of your quize",
         ("Easy","Medium","Hard"),
         index=None
        )
    # if option:
    #     st.markdown(f"You selected: **{option}**")
    # else:
    #     st.error("You must select Option")
    
    button=st.button("Click the button to intiate AI")


if button:
    if not images:
        st.error("Upolad images")
    if not option:
        st.error("Select Diffucalty")
    if images and option:
        #note

        with st.container(border=True):
            st.subheader("Your Note")
            with st.spinner("AI is writing note"):
                 note=note_generator(pil_images)
                 st.markdown(note)
        #audio
        with st.container(border=True):
            st.subheader("Audio Transcript")
            with st.spinner("Auido making"):
                note=note.replace("#","")
                note=note.replace("$","")
                note=note.replace("*","")
                note=note.replace("`","")
                note=note.replace("-","")
                st.audio(audio_transcript(note))
        #quiz
        with st.container(border=True): 
            st.subheader(f"Quize ({option}) Diffculty")
            with st.spinner("AI is writing note"):
                 st.markdown(quiz_generator(pil_images,option))
