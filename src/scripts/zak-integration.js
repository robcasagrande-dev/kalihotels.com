/**
 * WuBook ZaK PMS Integration Script
 * Handles date formatting, room selection, and redirects to the booking engine
 */

export function redirectToBooking(params) {
  const { checkIn, checkOut, guests, hotel } = params;

  // Base WuBook URL
  const wubookBase = 'https://wubook.net/nneb/mprop';
  const defaultEp = '4e454d97';
  const defaultWId = '4791';

  // Format dates: WuBook expects dates in DD/MM/YYYY or similar depending on configuration.
  // We will compute nights (n) between check-in and check-out.
  const checkInDate = new Date(checkIn);
  const checkOutDate = new Date(checkOut);
  
  let nights = 1;
  if (checkInDate && checkOutDate && checkOutDate > checkInDate) {
    const diffTime = Math.abs(checkOutDate - checkInDate);
    nights = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  }

  // Format date to DD/MM/YYYY
  const day = String(checkInDate.getDate()).padStart(2, '0');
  const month = String(checkInDate.getMonth() + 1).padStart(2, '0');
  const year = checkInDate.getFullYear();
  const formattedCheckIn = `${day}/${month}/${year}`;

  // Build booking URL query params
  // f: check-in date
  // n: nights
  // ep: multi-property token/key
  // w_id: widget ID
  // ad: adults (guests)
  const queryParams = new URLSearchParams({
    f: formattedCheckIn,
    n: String(nights),
    ep: defaultEp,
    w_id: defaultWId,
    ad: String(guests || 2)
  });

  // If a specific hotel code is selected, we can append it or route to a single-property booking page
  if (hotel && hotel !== 'all') {
    queryParams.set('h', hotel); // or corresponding single property parameter
  }

  const finalUrl = `${wubookBase}?${queryParams.toString()}`;
  return finalUrl;
}
