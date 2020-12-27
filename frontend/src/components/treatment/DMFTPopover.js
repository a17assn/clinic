import React, { useState } from 'react';
import { Radio } from 'antd';
import TreatmentsPopoverDrawer from './TreatmentsPopoverDrawer';
import axios from 'axios';

const RadioGroup = Radio.Group;

const DMFTPopover = (props) => {

   const [treatments, setTreatments] = useState([]);


   const getTreatments = (toothPosition) => {
      axios.get(`treatments/t/${toothPosition}-${props.patientId}`)
         .then((response) => {
            if (response.status === 200) {
               setTreatments(response.data.treatments);

            }
         })
         .catch((err) => {
            console.error(err);
            // message.error('Something went wrong! Please, try again.');
         });
      console.log('a', toothPosition)

   }

   const onChange = (e) => {
      props.onChange(props.toothPosition, e.target.value);
   }

   const radioStyle = {
      display: 'block',
      height: '30px',
      lineHeight: '30px',
   };

   const DMFTRadioGroup = (
      <RadioGroup defaultValue="None" value={props.value || ""} onChange={onChange} >
         <Radio style={radioStyle} value="">None</Radio>
         <Radio style={radioStyle} value="Decayed">Decayed</Radio>
         <Radio style={radioStyle} value="Missing">Missing</Radio>
         <Radio style={radioStyle} value="Filled">Filled Teeth</Radio>
      </RadioGroup>);

   return (
      <TreatmentsPopoverDrawer getTreatments={() => getTreatments(props.toothPosition)} treatments={treatments} title={props.toothPosition} content={DMFTRadioGroup}>
         {props.children}
      </TreatmentsPopoverDrawer>

   );

}

export default DMFTPopover;