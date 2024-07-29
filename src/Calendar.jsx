import React from 'react';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from   
 '@fullcalendar/timegrid';   


function CalendarComponent() {
//   const [value, onChange] = useState(new Date());

  return (
    <FullCalendar
      plugins={[dayGridPlugin, timeGridPlugin]}
      initialView="timeGridDay" // You can change this to 'timeGridWeek' for weekly view
    />
  );
}

export default CalendarComponent;
