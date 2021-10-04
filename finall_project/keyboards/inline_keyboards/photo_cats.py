from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cat_markup =InlineKeyboardMarkup(row_width=3)
red_cat_button = InlineKeyboardButton(text=" Red cat", callback_data="redcat",
                                      url="https://previews.123rf.com/images/evdoha/evdoha1710/evdoha171000096/87547104"
                                          "-beautiful-big-red-cat-on-the-windowsill.jpg")
cat_markup.insert(red_cat_button)
black_cat_button = InlineKeyboardButton(text='Black cat', callback_data="blackcat",
                                        url="https://www.thesprucepets.com/thmb/DvxumVXUoBY2q0k3VVnOFRRz-dw=/960x0/filt"
                                            "ers:no_upscale():max_bytes(150000):strip_icc():format(webp)/facts-about-b"
                                            "lack-cats-554102-hero-7281a22d75584d448290c359780c2ead.jpg")
white_cat_button = InlineKeyboardButton(text='White cat',callback_data="whitecat",
                                        url="https://www.thesprucepets.com/thmb/wWZ_Mympqnlq6hUbrnK6p2wIERk=/960x0/fil"
                                            "ters:no_upscale():max_bytes(150000):strip_icc():format(webp)/twenty20_e47b"
                                            "3798-dd9b-40b1-91ef-1d820337966e-5aa3f798642dca00363b0df1.jpg")
cat_markup.insert(black_cat_button)
cat_markup.insert(white_cat_button)

return_markup = InlineKeyboardMarkup(row_width=1)
return_button = InlineKeyboardButton(text="Return to prev page", callback_data="return")
return_markup.insert(return_button)