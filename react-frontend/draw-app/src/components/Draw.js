import React, { useRef, useState } from 'react'
import { SketchField, Tools } from 'react-sketch'
import { Button, Alert } from 'react-bootstrap'
import { saveAs } from 'file-saver'
import axios from 'axios'

const styles={
    draw: {
        margin: '0 auto'
    }
}

const Draw = () => {

    const [send, setSend] = useState(false)   
    const [result, setResult] = useState(null) 
    const sketch = useRef()

    const handleSubmit = () => {
        const canvas = sketch.current.toDataURL()
        // saveAs(canvas, 'digit.jpg')
        sendData(canvas)
    }

    const handleReset = () => {
        sketch.current.clear()
        sketch.current._backgroundColor('black')
        setSend(false)
        setResult()
    }

    const sendData = (canvas) => {
        console.log(canvas)

        const headers = {
            'accept': 'application/json'
        }

        const fdata = new FormData()
        fdata.append('image', canvas)

        axios.post('http://127.0.0.1:8000/digits-api/digit_classifier/', fdata, {headers:headers})
        .then(res => {
            console.log(res.data)
            setSend(true)
            getImageResult(res.data.id)
        })
        .catch(err =>
            console.log(err))
    }

    const getImageResult = (id) => {
        axios.get(`http://127.0.0.1:8000/digits-api/digit_classifier/${id}/`)
        .then(res => {
            setResult(res.data.result)
        })
    }

    return (
        <React.Fragment>
            {send && <Alert variant={"info"}>Drawing saved successfully for classification.</Alert>} 
            {result && <h3>Your digit is {result}</h3>} 

            <SketchField 
                ref={sketch}
                height='800px'
                width='800px'
                style={styles.draw}
                tool={Tools.Pencil}
                backgroundColor='black'
                lineColor='white'
                imgFormat='jpg'
                lineWidth={60}
            />
            <div className='mt-3'>
                <Button variant='primary' onClick={handleSubmit}>Send</Button>
                <Button variant='secondary' onClick={handleReset}>Reset</Button>
            </div>
        </React.Fragment>
    )
}

export default Draw
