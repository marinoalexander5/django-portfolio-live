import React, { useRef } from 'react'
import { SketchField, Tools } from 'react-sketch'
import { Button } from 'react-bootstrap'
import { saveAs } from 'file-saver'


const styles={
    draw: {
        margin: '0 auto'
    }
}

const Draw = () => {

    const sketch = useRef()

    const handleSubmit = () => {
        const canvas = sketch.current.toDataURL()
        saveAs(canvas, 'digit.jpg')
        sendData(canvas)
    }

    const handleReset = () => {
        sketch.current.clear()
        sketch.current._backgroundColor('black')
    }

    const sendData = (canvas) => {
        console.log(canvas)
    }

    const getImageResult = (id) => {
        console.log(id)
    }

    return (
        <React.Fragment>
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
                <Button variant='primary' onClick={handleSubmit}>Save</Button>
                <Button variant='secondary' onClick={handleReset}>Reset</Button>
            </div>
        </React.Fragment>
    )
}

export default Draw
