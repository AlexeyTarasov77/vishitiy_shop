// document.addEventListener('DOMContentLoaded', function() {
//     // const phoneInput = document.getElementById('phone_number');
//     const postIndex = document.getElementById('id_post');

//     phoneInput.addEventListener('input', validatePhoneNumber);
//     postIndex.addEventListener('input', validatePhoneNumber);
// });

// function validatePhoneNumber(event) {
//     const input = event.target;
//     const validCharacters = /^[0-9+\-()\s]*$/;
    
//     if (!validCharacters.test(input.value)) {
//         // Удаляем все недопустимые символы
//         input.value = input.value.replace(/[^0-9+\-()\s]/g, '');
//     }
// }


// id_post



document.addEventListener('DOMContentLoaded', function() {
    // const phoneNumberInput = document.getElementById('phone_number');
    const postIndexInput = document.getElementById('id_post');
    const userNameInput = document.getElementById('id_name');
    const userEmailInput = document.getElementById('id_email');
    
    // phoneNumberInput.addEventListener('input', function() {
    //     const maxLength = 20;
    //     if (phoneNumberInput.value.length > maxLength) {
    //         phoneNumberInput.value = phoneNumberInput.value.slice(0, maxLength);
    //     }
    // });

    postIndexInput.addEventListener('input', function() {
        const maxLength = 10;
        if (postIndexInput.value.length > maxLength) {
            postIndexInput.value = postIndexInput.value.slice(0, maxLength);
        }
    });

    userNameInput.addEventListener('input', function() {
        const maxLength = 25;
        if (userNameInput.value.length > maxLength) {
            userNameInput.value = userNameInput.value.slice(0, maxLength);
        }
    });


    userEmailInput.addEventListener('input', function() {
        const maxLength = 254;
        if (userEmailInput.value.length > maxLength) {
            userEmailInput.value = userEmailInput.value.slice(0, maxLength);
        }
    });



});



// 253 countries
const countries = [
    { name: "Afghanistan", code: "AF", phone: 93, format: "+93 70 000 0000" },
    { name: "Aland Islands", code: "AX", phone: 358, format: "+358 50 123 4567" },
    { name: "Albania", code: "AL", phone: 355, format: "+355 69 123 4567" },
    { name: "Algeria", code: "DZ", phone: 213, format: "+213 5 123 4567" },
    { name: "American Samoa", code: "AS", phone: 1684, format: "+1 684 123 4567" },
    { name: "Andorra", code: "AD", phone: 376, format: "+376 123 456" },
    { name: "Angola", code: "AO", phone: 244, format: "+244 912 345 678" },
    { name: "Anguilla", code: "AI", phone: 1264, format: "+1 264 123 4567" },
    { name: "Antarctica", code: "AQ", phone: 672, format: "+672 1 234 567" },
    { name: "Antigua and Barbuda", code: "AG", phone: 1268, format: "+1 268 123 4567" },
    { name: "Argentina", code: "AR", phone: 54, format: "+54 9 11 1234 5678" },
    { name: "Armenia", code: "AM", phone: 374, format: "+374 55 123 456" },
    { name: "Aruba", code: "AW", phone: 297, format: "+297 582 1234" },
    { name: "Australia", code: "AU", phone: 61, format: "+61 4 00 000 000" },
    { name: "Austria", code: "AT", phone: 43, format: "+43 6 50 000 0000" },
    { name: "Azerbaijan", code: "AZ", phone: 994, format: "+994 70 000 00 00" },
    { name: "Bahamas", code: "BS", phone: 1242, format: "+1 242 123 4567" },
    { name: "Bahrain", code: "BH", phone: 973, format: "+973 3 123 4567" },
    { name: "Bangladesh", code: "BD", phone: 880, format: "+880 1 234 5678" },
    { name: "Barbados", code: "BB", phone: 1246, format: "+1 246 123 4567" },
    { name: "Belarus", code: "BY", phone: 375, format: "+375 29 123 4567" },
    { name: "Belgium", code: "BE", phone: 32, format: "+32 478 12 34 56" },
    { name: "Belize", code: "BZ", phone: 501, format: "+501 600 1234" },
    { name: "Benin", code: "BJ", phone: 229, format: "+229 97 00 00 00" },
    { name: "Bermuda", code: "BM", phone: 1441, format: "+1 441 123 4567" },
    { name: "Bhutan", code: "BT", phone: 975, format: "+975 17 123 456" },
    { name: "Bolivia", code: "BO", phone: 591, format: "+591 2 123 4567" },
    { name: "Bonaire, Sint Eustatius and Saba", code: "BQ", phone: 599, format: "+599 701 2345" },
    { name: "Bosnia and Herzegovina", code: "BA", phone: 387, format: "+387 61 123 456" },
    { name: "Botswana", code: "BW", phone: 267, format: "+267 71 123 456" },
    { name: "Bouvet Island", code: "BV", phone: 55, format: "+55 21 1234 5678" },
    { name: "Brazil", code: "BR", phone: 55, format: "+55 11 91234 5678" },
    { name: "British Indian Ocean Territory", code: "IO", phone: 246, format: "+246 123 4567" },
    { name: "Brunei Darussalam", code: "BN", phone: 673, format: "+673 123 4567" },
    { name: "Bulgaria", code: "BG", phone: 359, format: "+359 88 123 4567" },
    { name: "Burkina Faso", code: "BF", phone: 226, format: "+226 70 00 00 00" },
    { name: "Burundi", code: "BI", phone: 257, format: "+257 71 123 456" },
    { name: "Cambodia", code: "KH", phone: 855, format: "+855 12 345 678" },
    { name: "Cameroon", code: "CM", phone: 237, format: "+237 6 123 4567" },
    { name: "Canada", code: "CA", phone: 1, format: "+1 123 456 7890" },
    { name: "Cape Verde", code: "CV", phone: 238, format: "+238 91 123 456" },
    { name: "Cayman Islands", code: "KY", phone: 1345, format: "+1 345 123 4567" },
    { name: "Central African Republic", code: "CF", phone: 236, format: "+236 70 123 456" },
    { name: "Chad", code: "TD", phone: 235, format: "+235 99 12 34 56" },
    { name: "Chile", code: "CL", phone: 56, format: "+56 9 1234 5678" },
    { name: "China", code: "CN", phone: 86, format: "+86 138 1234 5678" },
    { name: "Christmas Island", code: "CX", phone: 61, format: "+61 8 9111 1234" },
    { name: "Cocos (Keeling) Islands", code: "CC", phone: 672, format: "+672 1 234 567" },
    { name: "Colombia", code: "CO", phone: 57, format: "+57 1 234 5678" },
    { name: "Comoros", code: "KM", phone: 269, format: "+269 300 1234" },
    { name: "Congo", code: "CG", phone: 242, format: "+242 06 123 456" },
    { name: "Congo, Democratic Republic of the Congo", code: "CD", phone: 242, format: "+243 81 234 5678" },
    { name: "Cook Islands", code: "CK", phone: 682, format: "+682 20 12345" },
    { name: "Costa Rica", code: "CR", phone: 506, format: "+506 800 1234" },
    { name: "Cote D'Ivoire", code: "CI", phone: 225, format: "+225 07 12 34 56" },
    { name: "Croatia", code: "HR", phone: 385, format: "+385 91 123 4567" },
    { name: "Cuba", code: "CU", phone: 53, format: "+53 5 123 4567" },
    { name: "Curacao", code: "CW", phone: 599, format: "+599 9 123 4567" },
    { name: "Cyprus", code: "CY", phone: 357, format: "+357 99 123456" },
    { name: "Czech Republic", code: "CZ", phone: 420, format: "+420 777 123 456" },
    { name: "Denmark", code: "DK", phone: 45, format: "+45 12 34 56 78" },
    { name: "Djibouti", code: "DJ", phone: 253, format: "+253 77 123 456" },
    { name: "Dominica", code: "DM", phone: 1767, format: "+1 767 123 4567" },
    { name: "Dominican Republic", code: "DO", phone: 1809, format: "+1 809 123 4567" },
    { name: "Ecuador", code: "EC", phone: 593, format: "+593 2 123 4567" },
    { name: "Egypt", code: "EG", phone: 20, format: "+20 10 123 4567" },
    { name: "El Salvador", code: "SV", phone: 503, format: "+503 7123 4567" },
    { name: "Equatorial Guinea", code: "GQ", phone: 240, format: "+240 222 123 456" },
    { name: "Eritrea", code: "ER", phone: 291, format: "+291 7 123 456" },
    { name: "Estonia", code: "EE", phone: 372, format: "+372 50 12345" },
    { name: "Eswatini", code: "SZ", phone: 268, format: "+268 76 123 456" },
    { name: "Ethiopia", code: "ET", phone: 251, format: "+251 91 123 4567" },
    { name: "Falkland Islands", code: "FK", phone: 500, format: "+500 12345" },
    { name: "Faroe Islands", code: "FO", phone: 298, format: "+298 20 123" },
    { name: "Fiji", code: "FJ", phone: 679, format: "+679 123 4567" },
    { name: "Finland", code: "FI", phone: 358, format: "+358 40 123 4567" },
    { name: "France", code: "FR", phone: 33, format: "+33 6 12 34 56 78" },
    { name: "French Guiana", code: "GF", phone: 594, format: "+594 694 12 34 56" },
    { name: "French Polynesia", code: "PF", phone: 689, format: "+689 87 12 34" },
    { name: "Gabon", code: "GA", phone: 241, format: "+241 07 12 34 56" },
    { name: "Gambia", code: "GM", phone: 220, format: "+220 123 4567" },
    { name: "Georgia", code: "GE", phone: 995, format: "+995 595 12 34 56" },
    { name: "Germany", code: "DE", phone: 49, format: "+49 170 1234567" },
    { name: "Ghana", code: "GH", phone: 233, format: "+233 20 123 4567" },
    { name: "Gibraltar", code: "GI", phone: 350, format: "+350 200 12345" },
    { name: "Greece", code: "GR", phone: 30, format: "+30 69 1234 5678" },
    { name: "Greenland", code: "GL", phone: 299, format: "+299 50 12 34" },
    { name: "Grenada", code: "GD", phone: 1473, format: "+1 473 123 4567" },
    { name: "Guadeloupe", code: "GP", phone: 590, format: "+590 690 12 34 56" },
    { name: "Guam", code: "GU", phone: 1671, format: "+1 671 123 4567" },
    { name: "Guatemala", code: "GT", phone: 502, format: "+502 1234 5678" },
    { name: "Guinea", code: "GN", phone: 224, format: "+224 622 123 456" },
    { name: "Guinea-Bissau", code: "GW", phone: 245, format: "+245 20 123 456" },
    { name: "Guyana", code: "GY", phone: 592, format: "+592 600 1234" },
    { name: "Haiti", code: "HT", phone: 509, format: "+509 29 12 34 56" },
    { name: "Honduras", code: "HN", phone: 504, format: "+504 1234 5678" },
    { name: "Hong Kong", code: "HK", phone: 852, format: "+852 9123 4567" },
    { name: "Hungary", code: "HU", phone: 36, format: "+36 20 123 4567" },
    { name: "Iceland", code: "IS", phone: 354, format: "+354 123 4567" },
    { name: "India", code: "IN", phone: 91, format: "+91 987 654 3210" },
    { name: "Indonesia", code: "ID", phone: 62, format: "+62 812 3456 7890" },
    { name: "Iran", code: "IR", phone: 98, format: "+98 912 345 6789" },
    { name: "Iraq", code: "IQ", phone: 964, format: "+964 750 123 4567" },
    { name: "Ireland", code: "IE", phone: 353, format: "+353 87 123 4567" },
    { name: "Israel", code: "IL", phone: 972, format: "+972 50 123 4567" },
    { name: "Italy", code: "IT", phone: 39, format: "+39 345 678 9012" },
    { name: "Jamaica", code: "JM", phone: 1876, format: "+1 876 123 4567" },
    { name: "Japan", code: "JP", phone: 81, format: "+81 90 1234 5678" },
    { name: "Jordan", code: "JO", phone: 962, format: "+962 79 123 4567" },
    { name: "Kazakhstan", code: "KZ", phone: 7, format: "+7 701 123 4567" },
    { name: "Kenya", code: "KE", phone: 254, format: "+254 700 123 456" },
    { name: "Kiribati", code: "KI", phone: 686, format: "+686 80 123" },
    { name: "Korea, North", code: "KP", phone: 850, format: "+850 2 123 4567" },
    { name: "Korea, South", code: "KR", phone: 82, format: "+82 10 1234 5678" },
    { name: "Kuwait", code: "KW", phone: 965, format: "+965 512 3456" },
    { name: "Kyrgyzstan", code: "KG", phone: 996, format: "+996 500 123 456" },
    { name: "Lao People's Democratic Republic", code: "LA", phone: 856, format: "+856 20 123 456" },
    { name: "Latvia", code: "LV", phone: 371, format: "+371 20 123 456" },
    { name: "Lebanon", code: "LB", phone: 961, format: "+961 3 123 456" },
    { name: "Lesotho", code: "LS", phone: 266, format: "+266 500 1234" },
    { name: "Liberia", code: "LR", phone: 231, format: "+231 77 123 456" },
    { name: "Libya", code: "LY", phone: 218, format: "+218 91 234 5678" },
    { name: "Liechtenstein", code: "LI", phone: 423, format: "+423 123 456" },
    { name: "Lithuania", code: "LT", phone: 370, format: "+370 600 12345" },
    { name: "Luxembourg", code: "LU", phone: 352, format: "+352 621 12 34 56" },
    { name: "Madagascar", code: "MG", phone: 261, format: "+261 32 12 34 56" },
    { name: "Malawi", code: "MW", phone: 265, format: "+265 99 123 456" },
    { name: "Malaysia", code: "MY", phone: 60, format: "+60 12 345 6789" },
    { name: "Maldives", code: "MV", phone: 960, format: "+960 7 123 456" },
    { name: "Mali", code: "ML", phone: 223, format: "+223 76 12 34 56" },
    { name: "Malta", code: "MT", phone: 356, format: "+356 79 123 456" },
    { name: "Marshall Islands", code: "MH", phone: 692, format: "+692 123 4567" },
    { name: "Mauritania", code: "MR", phone: 222, format: "+222 32 12 34 56" },
    { name: "Mauritius", code: "MU", phone: 230, format: "+230 123 4567" },
    { name: "Mayotte", code: "YT", phone: 262, format: "+262 639 12 34 56" },
    { name: "Mexico", code: "MX", phone: 52, format: "+52 55 1234 5678" },
    { name: "Micronesia", code: "FM", phone: 691, format: "+691 123 4567" },
    { name: "Moldova", code: "MD", phone: 373, format: "+373 69 123 456" },
    { name: "Monaco", code: "MC", phone: 377, format: "+377 6 12 34 56" },
    { name: "Mongolia", code: "MN", phone: 976, format: "+976 9912 3456" },
    { name: "Montenegro", code: "ME", phone: 382, format: "+382 67 123 456" },
    { name: "Montserrat", code: "MS", phone: 1664, format: "+1 664 123 4567" },
    { name: "Morocco", code: "MA", phone: 212, format: "+212 6 123 4567" },
    { name: "Mozambique", code: "MZ", phone: 258, format: "+258 84 123 456" },
    { name: "Myanmar", code: "MM", phone: 95, format: "+95 9 123 4567" },
    { name: "Namibia", code: "NA", phone: 264, format: "+264 81 123 4567" },
    { name: "Nauru", code: "NR", phone: 674, format: "+674 123 456" },
    { name: "Nepal", code: "NP", phone: 977, format: "+977 980 123 4567" },
    { name: "Netherlands", code: "NL", phone: 31, format: "+31 6 1234 5678" },
    { name: "New Caledonia", code: "NC", phone: 687, format: "+687 75 12 34" },
    { name: "New Zealand", code: "NZ", phone: 64, format: "+64 21 123 456" },
    { name: "Nicaragua", code: "NI", phone: 505, format: "+505 8888 8888" },
    { name: "Niger", code: "NE", phone: 227, format: "+227 91 23 45 67" },
    { name: "Nigeria", code: "NG", phone: 234, format: "+234 802 123 4567" },
    { name: "Niue", code: "NU", phone: 683, format: "+683 1234" },
    { name: "Norfolk Island", code: "NF", phone: 672, format: "+672 3 1234" },
    { name: "North Macedonia", code: "MK", phone: 389, format: "+389 70 123 456" },
    { name: "Northern Mariana Islands", code: "MP", phone: 1670, format: "+1 670 123 4567" },
    { name: "Norway", code: "NO", phone: 47, format: "+47 912 34 567" },
    { name: "Oman", code: "OM", phone: 968, format: "+968 9 123 4567" },
    { name: "Pakistan", code: "PK", phone: 92, format: "+92 300 123 4567" },
    { name: "Palau", code: "PW", phone: 680, format: "+680 488 1234" },
    { name: "Palestine", code: "PS", phone: 970, format: "+970 599 123 456" },
    { name: "Panama", code: "PA", phone: 507, format: "+507 6123 4567" },
    { name: "Papua New Guinea", code: "PG", phone: 675, format: "+675 7123 456" },
    { name: "Paraguay", code: "PY", phone: 595, format: "+595 991 123 456" },
    { name: "Peru", code: "PE", phone: 51, format: "+51 992 123 456" },
    { name: "Philippines", code: "PH", phone: 63, format: "+63 912 345 6789" },
    { name: "Pitcairn", code: "PN", phone: 64, format: "+64 9 123 4567" },
    { name: "Poland", code: "PL", phone: 48, format: "+48 601 123 456" },
    { name: "Portugal", code: "PT", phone: 351, format: "+351 912 345 678" },
    { name: "Puerto Rico", code: "PR", phone: 1939, format: "+1 939 123 4567" },
    { name: "Qatar", code: "QA", phone: 974, format: "+974 555 12345" },
    { name: "Romania", code: "RO", phone: 40, format: "+40 722 123 456" },
    { name: "Russia", code: "RU", phone: 7, format: "+7 900 123 4567" },
    { name: "Rwanda", code: "RW", phone: 250, format: "+250 78 123 456" },
    { name: "Saint Barthelemy", code: "BL", phone: 590, format: "+590 690 12 34 56" },
    { name: "Saint Helena", code: "SH", phone: 290, format: "+290 12345" },
    { name: "Saint Kitts and Nevis", code: "KN", phone: 1869, format: "+1 869 123 4567" },
    { name: "Saint Lucia", code: "LC", phone: 1758, format: "+1 758 123 4567" },
    { name: "Saint Martin", code: "MF", phone: 590, format: "+590 690 12 34 56" },
    { name: "Saint Pierre and Miquelon", code: "PM", phone: 508, format: "+508 41 23 45" },
    { name: "Saint Vincent and the Grenadines", code: "VC", phone: 1784, format: "+1 784 123 4567" },
    { name: "Samoa", code: "WS", phone: 685, format: "+685 75 123 45" },
    { name: "San Marino", code: "SM", phone: 378, format: "+378 0549 12345" },
    { name: "Sao Tome and Principe", code: "ST", phone: 239, format: "+239 222 1234" },
    { name: "Saudi Arabia", code: "SA", phone: 966, format: "+966 55 123 4567" },
    { name: "Senegal", code: "SN", phone: 221, format: "+221 77 123 4567" },
    { name: "Serbia", code: "RS", phone: 381, format: "+381 60 123 4567" },
    { name: "Seychelles", code: "SC", phone: 248, format: "+248 2 123 456" },
    { name: "Sierra Leone", code: "SL", phone: 232, format: "+232 76 123 456" },
    { name: "Singapore", code: "SG", phone: 65, format: "+65 9123 4567" },
    { name: "Sint Maarten", code: "SX", phone: 1721, format: "+1 721 123 4567" },
    { name: "Slovakia", code: "SK", phone: 421, format: "+421 911 123 456" },
    { name: "Slovenia", code: "SI", phone: 386, format: "+386 40 123 456" },
    { name: "Solomon Islands", code: "SB", phone: 677, format: "+677 74 123" },
    { name: "Somalia", code: "SO", phone: 252, format: "+252 6 123 4567" },
    { name: "South Africa", code: "ZA", phone: 27, format: "+27 71 123 4567" },
    { name: "South Sudan", code: "SS", phone: 211, format: "+211 912 345 678" },
    { name: "Spain", code: "ES", phone: 34, format: "+34 612 34 56 78" },
    { name: "Sri Lanka", code: "LK", phone: 94, format: "+94 71 123 4567" },
    { name: "Sudan", code: "SD", phone: 249, format: "+249 912 345 678" },
    { name: "Suriname", code: "SR", phone: 597, format: "+597 88 123 456" },
    { name: "Sweden", code: "SE", phone: 46, format: "+46 70 123 4567" },
    { name: "Switzerland", code: "CH", phone: 41, format: "+41 79 123 45 67" },
    { name: "Syria", code: "SY", phone: 963, format: "+963 9 123 4567" },
    { name: "Taiwan", code: "TW", phone: 886, format: "+886 912 345 678" },
    { name: "Tajikistan", code: "TJ", phone: 992, format: "+992 90 123 4567" },
    { name: "Tanzania", code: "TZ", phone: 255, format: "+255 755 123 456" },
    { name: "Thailand", code: "TH", phone: 66, format: "+66 81 234 5678" },
    { name: "Timor-Leste", code: "TL", phone: 670, format: "+670 77 123 456" },
    { name: "Togo", code: "TG", phone: 228, format: "+228 90 12 34 56" },
    { name: "Tokelau", code: "TK", phone: 690, format: "+690 12 34" },
    { name: "Tonga", code: "TO", phone: 676, format: "+676 12345" },
    { name: "Trinidad and Tobago", code: "TT", phone: 1868, format: "+1 868 123 4567" },
    { name: "Tunisia", code: "TN", phone: 216, format: "+216 98 123 456" },
    { name: "Turkey", code: "TR", phone: 90, format: "+90 532 123 4567" },
    { name: "Turkmenistan", code: "TM", phone: 993, format: "+993 62 123 456" },
    { name: "Tuvalu", code: "TV", phone: 688, format: "+688 12 345" },
    { name: "Uganda", code: "UG", phone: 256, format: "+256 70 123 4567" },
    { name: "Ukraine", code: "UA", phone: 380, format: "+380 50 123 4567" },
    { name: "United Arab Emirates", code: "AE", phone: 971, format: "+971 50 123 4567" },
    { name: "United Kingdom", code: "GB", phone: 44, format: "+44 7911 123456" },
    { name: "United States", code: "US", phone: 1, format: "+1 123 456 7890" }
]

const select_box = document.querySelector('.options');
const search_box = document.querySelector('.search-box');
const input_box = document.querySelector('input[type="tel"]');
const selected_option = document.querySelector('.selected-option div');
const country_code = document.querySelector('.country-code');
const error_message = document.querySelector('.error-message'); // Элемент для сообщения об ошибке

let options = null;

for (const country of countries) {
    const option = `
    <li class="option">
        <div>
            <span class="iconify" data-icon="flag:${country.code.toLowerCase()}-4x3"></span>
            <span class="country-name">${country.name}</span>
        </div>
        <strong>+${country.phone}</strong>
    </li> `;

    select_box.querySelector('ol').insertAdjacentHTML('beforeend', option);
    options = document.querySelectorAll('.option');
}

function selectOption() {
    const icon = this.querySelector('.iconify').cloneNode(true),
        phone_code = this.querySelector('strong').cloneNode(true);

    selected_option.innerHTML = '';
    selected_option.append(icon, phone_code);

    // Устанавливаем значение кода страны в скрытое поле и отображаем его рядом с полем ввода
    country_code.innerText = phone_code.innerText;
    input_box.dataset.countryCode = phone_code.innerText;

    select_box.classList.remove('active');
    selected_option.classList.remove('active');

    search_box.value = '';
    select_box.querySelectorAll('.hide').forEach(el => el.classList.remove('hide'));
}

function searchCountry() {
    let search_query = search_box.value.toLowerCase();
    for (const option of options) {
        let is_matched = option.querySelector('.country-name').innerText.toLowerCase().includes(search_query);
        option.classList.toggle('hide', !is_matched);
    }
}

selected_option.addEventListener('click', () => {
    select_box.classList.toggle('active');
    selected_option.classList.toggle('active');
});

options.forEach(option => option.addEventListener('click', selectOption));
search_box.addEventListener('input', searchCountry);

// Функция для форматирования номера телефона
function formatPhoneNumber(input) {
    // Удалить все символы, кроме цифр
    const cleaned = ('' + input).replace(/\D/g, '');

    // Форматирование номера
    const match = cleaned.match(/^(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})$/);

    if (match) {
        return `${match[1]}${match[1] ? ' ' : ''}${match[2]}${match[2] ? '-' : ''}${match[3]}${match[3] ? '-' : ''}${match[4]}`.replace(/-+$/, '');
    }

    return input;
}

// Добавляем обработчик события для форматирования номера телефона при вводе
input_box.addEventListener('input', () => {
    const number = input_box.value;
    input_box.value = formatPhoneNumber(number);
});

// Функция для проверки валидности номера телефона
function validatePhoneNumber() {
    const cleaned = ('' + input_box.value).replace(/\D/g, '');
    const countryCode = input_box.dataset.countryCode ? input_box.dataset.countryCode.trim().replace(/\D/g, '') : '';

    if (cleaned.length === 0 || (countryCode === '380' && cleaned.length < 9) || (countryCode !== '380' && cleaned.length < 4)) {
        error_message.style.display = 'block';
        return false;
    }

    error_message.style.display = 'none';
    return true;
}

// Обработчик события для кнопки отправки формы
document.querySelector('button[type="submit"]').addEventListener('click', (event) => {
    if (!validatePhoneNumber()) {
        event.preventDefault(); // Не отправлять форму, если номер телефона не валидный
    }
});