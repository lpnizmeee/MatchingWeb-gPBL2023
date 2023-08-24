import React from 'react';
import ReactMapGL from 'react-map-gl';

function Mapbox() {
    const [viewport, setViewport] = React.useState({
        latitude: 37,7577,
        longitude: -122,2,
        zoom:8,
    });
    return (
        <ReactMapGL
        {...viewport}
        width:"100%"
        height:"100%"
        onVie

        />
    )
}