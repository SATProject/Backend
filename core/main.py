import random

happiness = [
    "خوب",
    "خوشحال",
    "شاد",
    "خندان",
    "عالی",
    "خوشبخت",
    "خوش",
    "بهتر"
]
sadness = [
    "بد",
    "ناراحت",
    "غم",
    "غمگین",
    "آشفته",
    "پریشان",
]

negative_verbs = [
    "نیست",
    "ندار",
    "نمیکن",
    "نمی کن",
    "نمی‌کن"
]

yes = [
    "بله",
    "آره",
    "اره",
    "باشه",
    "اوکی",
    "میدم",
    "می‌دم"
]

no = [
    "خیر",
    "نه",
    "نمی"
]

positive_emotions = [
    "HAPPY"
]

negative_emotions = [
    "SAD"
]

recent = [
    "اخیرا",
    "تازگی",
    "تازگیا",
    "تازه",
    "نزدیک"
]

long_time = [
    "خیلی",
    "پیش",
    "قدیما",
    "قدیم",
    "خیلی وقت پیش"
]


greeting = [
    "سلام",
    "سلام. من قراه کمکت کنم حالت بهتر بشه.",
    "درود",
    "سلام و درود"
]

feeling = [
   "حالت چطوره؟",
    "خوبی؟",
    "چطوری؟",
    "امروز حالت خوبه؟",
    "امروز حالت چطوره؟",
]

emotion_verifier = [
    "آیا احساس X می‌کنی؟",
    "آیا حس X داری؟"
]

tell_emotion = [
    "ناراحتی یا خوشحالی؟",
    "احساس خوشحال می‌کنی یا ناراحتی؟"
]

if_need_any_protocols = [
    "آیا نیاز به تمرینی برای بهبود حالت داری؟",
    "آیا به تمرینی برای بهتر شدن حالت احتیاج داری؟",
    "آیا حس می‌کنی احتیاج به تمرینی داشته باشی؟"
]


event = [
    "متاسفم که می شنوم حالت خوب نیست. آیا اتفاق خاصی افتاده که این احساس را در شما ایجاد کند؟",
    "آیا اتفاق خاصی افتاده که غمگینت کنه؟ سعی کن باهام راحت باشی.",
    "اتفاق خاصی افتاده که غمگینت کنه؟ سعی کن باهام راحت باشی.",
    "اتفاق خاصی افتاده که ناراحتت کنه؟",
    "چیز خاصی شده که باعث شده ناراحت باشی؟",
    "اتفاقی هست که ناراحتت کرده؟"
]

time = [
    "این اتفاق اخیرا رخ داده یا مدت‌ها پیش؟",
    "تازگیا این اتفاق افتاده؟",
    "اخیرا این اتفاق پیش اومده؟",
    "این اتفاق برای چیزی است که اخیرا رخ داده یا مدت‌ها پیش اتفاق افتاده؟",
    "اخیرا این اتفاق رخ داده؟"
]

additionals =  [
    {
    "questions": [ 
        "آیا اخیرا یکی از احساسات حسادت یا حرص رو داشتی؟",
        "آیا تازگیا یکی از احساسات حسادت یا حرص رو داشتی؟",
        "آیا اخیرا احساس حسادت یا حرص کردی؟",
        "آیا تازگیا احساس حسادت یا حرص کردی؟",
        "آیا اخیرا حس حسادت یا حرص داشتی",
        "آیا تازگیا حس حسادت یا حرص داشتی"
        ], 
        "YES":[16, 18, 19], "NO":[16]
    },
    {
    "questions": [ 
        "آیا حس می‌کنی که باید ناجی فرد دیگری باشی؟",
        "آیا حس می‌کنی که باید نجات‌دهنده فرد دیگری باشی؟",
        "آیا احساس می‌کنی که باید برای یک فرد دیگه نجات‌دهنده باشی؟",
        "آیا احساس می‌کنی که باید برای یک فرد دیگه ناجی باشی؟"
        ], 
        "YES":[12, 21, 25], "NO":[16]
    },
    {
    "questions": [ 
        "آیا احساس این رو داری که قربانی یه نفر دیگه هستی؟",
        "آیا احساس اینو داری که قربانی یه نفره دیگه‌ای؟"
        ], 
        "YES":[12, 21, 25], "NO":[16]
    },
    {
    "questions": [ 
        "آیا احساس این رو داری که برای یه نفر دیگه داری فدا میشی؟",
        "آیا احساس این رو داری که برای یه نفر دیگه داری قربانی میشی؟",
        "آیا حس قربانی شدن برای یه نفر دیگه رو داری؟",
        "آیا حس فدا شدن برای یه نفر دیگه رو داری؟"
        ], 
        "YES":[12, 21, 25], "NO":[16]
    },
    {
    "questions": [ 
        "آیا حس می‌کنی که شخص دیگری رو داری کنترل می‌کنی؟",
        "آیا احساس اینو داری که شخص دیگری رو داری کنترل می‌کنی؟",
        "آیا احساس اینو داری که شخص دیگه‌ای رو کنترل می‌کنی یا بهش جهت میدی؟",
        "آیا حس می‌کنی که شخص دیگه‌ای رو کنترل می‌کنی یا بهش جهت میدی؟"
        ], 
        "YES":[12, 21, 25], "NO":[16]
    },
    {
    "questions": [ 
        "آیا همیشه وقتی که چیزی بد پیش میره خودتو سرزنش می‌کنی؟",
        "آیا همیشه وقتی که چیزی بد پیش میره خودتو متهم می‌کنی؟",
        "آیا همیشه وقتی که چیزی بد پیش میره خودتو مقصر می‌دونی"
        ], 
        "YES":[12, 21, 25], "NO":[16]
    },
    {
    "questions": [ 
        "آیا همیشه نقطه نظرات دیگران رو توی کارات در نظر می‌کیری؟",
        "آیا همیشه نظرات دیگران رو توی کارات در نظر می‌کیری؟"
        ], 
        "YES":[16], "NO":[16, 21]
    },
    {
    "questions": [ 
        "آیا حس می‌کنی که داری به سمت یه بحران شخصیتی میری؟",
        "آیا فکر می‌کنی که داری به سمت یه بحران شخصیتی پیش میری؟",
        "آیا فکر می‌کنی که داری به یه بحران شخصیتی نزدیک میشی؟"
        ], 
        "YES":[16, 26], "NO":[16]
    }
]



protocol_titles = [
            "تمرین خاصی نیاز نیست.",
            "یادآوری خاطرات کودکی",
            "در آغوش گرفتن و آرامش دادن به کودک",
            "خواندن یک موسیقی محبت‌آمیز",
            "ابراز حس محبت و مراقبت از کودک",
            "تعهد به حمایت و مراقبت از کودک",
            "بازیابی دنیای عاطفی ما",
            "حفظ رابطه محبت آمیز با کودک و ایجاد اشتیاق برای زندگی",
            "لذت بردن از طبیعت",
            "غلبه بر احساسات منفی فعلی",
            "برآمدن از پس دردهای گذشته",
            "آرامش عضلانی و صورت شاد برای خندیدن عمدی",
            "خنده پیروزی بر خودمان",
            "خندیدن با خودِ کودکی‌مان",
            "خنده عمدی",
            "یاد بگیریم دیدگاه‌های خودمان را تغییر دهیم.",
            "یاد بگیریم در مورد دردهای گذشته‌مان شاد باشیم.",
            "شناسایی الگوهای بروز نارضایتی‌های شخصی",
            "برنامه ریزی برای اقدامات سازنده‌تر",
            "الگوی دلسوز خود را پیدا کنید و با آن پیوند برقرار کنید.",
            "به روز رسانی باورهای سفت و سخت ما برای افزایش خلاقیت",
            "تمرین عبارات تاکیدی",
            "استفاده از خنده برای کنار آمدن با یک تراژدی",
            "سعی کنید به تدریج از مدل کار درونی خود خود و تأثیر مراقبین اولیه و محیط اولیه خود آگاه شوید.",
            "شناسایی و مهار احساسات آزاردهنده داخلی",
            "حل بحران های شخصی",
            "کشف خودِ واقعی و مستقل در این زمان اضطرار",
        ]

protocols = [
            ["نیازی به تمرینی نیست."],
            ["در مکانی ساکت به عکس های شاد و ناراحت خود نگاه کنید. خاطرات مثبت و منفی دوران کودکی و روابط اولیه در خانواده را به یاد آورید."],
            [
                "۲- الف:",
                  "(۱) با چشمان بسته ابتدا عکس یا آواتار شاد خود را تصور کنید و تصور کنید کودک در نزدیکی شماست.",
                  "(۲) حال تصور کنید کودک را در آغوش گرفته اید.",
                  "(۳) سپس تصور کنید که درحال بازی با کودک هستید، به عنوان مثال؛ بازی‌هایی که در کودکی انجام داده اید.",
                  "(۴) در نهایت تصور کنید در حال رقصیدن با کودک هستید.",
                  "در مورد احساس خود در هر مرحله از (۱) تا (۴) فکر کنید.",
                "۲- ب:",
                  "(۱) با چشمان بسته، عکس یا آواتار ناراحت خود را تصور کنید که کودک نزدیک شماست.",
                  "(۲) حالا تصور کنید که کودک را در آغوش گرفته و دلداری می دهید.",
                  "(۳) چشمان خود را باز کنید، هدست واقعیت مجازی را روی صورتتان بگذارید.",
                    "(الف) یک احساس منفی (ناراحتی، عصبانیت، ترس یا انزجار) روی آواتار خود قرار دهید.",
                    "(ب) سپس بر روی «احساسات خودکار» کلیک کنید و با خیره شدن به آواتار کودکِ خود تصور کنید که به کودک اطمینان و آرامش می دهید که باعث خوشحالی و در نهایت رقص کودک می شود.",
                  "در مورد احساس خود در هر مرحله از (۱) تا (۳) فکر کنید.",
            ],
            ["کپی هایی از عکس شاد را برای نمایش در خانه، محل کار و کیف پول خود چاپ کنید. در نظر بگیرید که تصویر دیجیتال آن را به‌عنوان پس‌زمینه روی تلفن و لپ‌تاپ خود و دیگر دیوایس‌های دیجیتال تنظیم کنید. آهنگ شادی را که دوست دارید انتخاب کنید و احساسات گرما، محبت، عشق را القا کند. آهنگ را حفظ کنید و تا جایی که می توانید آن را در برنامه روزانه خود بخوانید. در حالی که به عکس یا آواتار شاد نگاه می کنید، آهنگ را بخوانید تا راهی برای ایجاد پیوند عاطفی عمیق با کودک در ذهن خود داشته باشید. بی سر و صدا شروع کنید؛ سپس، با گذشت زمان، اجازه دهید صدایتان بلندتر شود، در حالی که بیشتر از بدن خود استفاده می کنید (مثلاً شانه ها یا دستان خود را تکان دهید، و ابروهای خود را بالا و پایین ببرید). تصور کنید که به این ترتیب، مانند یک پدر یا مادر، گفتگوی پرشور و محبت آمیز دارید و با شادی با کودک می رقصید و بازی می کنید."],
            ["در حالی که از ته دل به عکس یا آواتار شاد لبخند می زنید، با صدای بلند به فرزندتان بگویید: «من عاشقانه دوستت دارم و عمیقاً به تو اهمیت می دهم»."],
            ["در این تمرین ما شروع به مراقبت از کودک مانند فرزند خود می کنیم. در ابتدا احساسات خود را به کودک نسبت می دهیم و سپس به عنوان خودمان، با تعهد در زمان و مکان خاصی شروع می کنیم. پس از خواندن با صدای آرام، با اطمینان این را با صدای بلند متعهد می‌شویم: «از این به بعد، به‌دنبال این هستم که به‌عنوان یک پدر یا مادر فداکار و دوست داشتنی نسبت به این کودک عمل کنم و به‌طور پیوسته و از صمیم قلب به هر طریق ممکن از او مراقبت کنم. من تمام تلاشم را برای حمایت از سلامت و رشد عاطفی این کودک انجام خواهم داد.»"],
            ["از طریق تخیل یا با نقاشی، دنیای عاطفی خود را خانه ای با قسمت های متروکه ای در نظر بگیرید که به طور کامل آن را بازسازی خواهید کرد. خانه جدید در نظر گرفته شده است تا در مواقع پریشانی پناهگاهی امن برای کودک و پایگاهی امن برای کودک برای مقابله با چالش های زندگی فراهم کند. خانه جدید و باغ آن روشن و آفتابی است. به این ترتیب تمرینات دلبستگی خود را در این محیط انجام خواهیم داد. زیرزمین بازسازی نشده خانه جدید بقایای خانه متروکه است و حاوی احساسات منفی ماست. هنگامی که احساسات منفی را تحمل می کنید، تصور کنید که کودک در زیرزمین به دام افتاده است، اما می تواند به تدریج یاد بگیرد که در زیرزمین را باز کند، بیرون برود و وارد اتاق های روشن شود و دوباره با بزرگسالان متحد شوید."],
            [
                "۷- الف: چند عبارت کوتاه را انتخاب کنید، به عنوان مثال، «تو فرزند زیبای من هستی» یا «عشقِ من». در حالی که به عکس یا آواتار شاد نگاه می کنید، آن را به آرامی، با صدای بلند، حداقل پنج بار بگویید. سپس آهنگ مورد علاقه خود را حداقل پنج بار بخوانید.",
                "۷- ب: در حالی که در آینه نگاه می کنید، تصویر خود را شبیه کودک (یعنی خودِ احساسی‌تان) تصور کنید، سپس شروع به خواندن آهنگ انتخابی قبلی خود با صدای بلند کنید. (اگر تصور کودک در آینه برایتان سخت است، عکس «شاد» کودک خود را در مقابل آینه قرار دهید و تمرین را انجام دهید و در حالی که به عکس کودکی شاد خود در آینه نگاه می کنید). این کار را ابتدا دو بار و سپس تا آنجا که ممکن است در شرایط مختلف در طول روز انجام دهید. مثلا در راه رفتن به محل کار یا هنگام پختن شام، تا آنها را در زندگی جدید خود ادغام کنید. هنگامی که خواندن آهنگ مورد علاقه شما به عادت شما تبدیل می شود، به ابزاری موثر برای تقویت تأثیرات مثبت و مدیریت احساسات تبدیل خواهد شد.",
            ],
            ["ایجاد دلبستگی به طبیعت برای فرزندتان راهی موثر برای افزایش شادی و کاهش احساسات منفی است. به یک باغ، پارک یا جنگل بروید. حداقل ۵ دقیقه را صرف تحسین یک درخت کنید و سعی کنید زیباییِ واقعی آن را که قبلاً هرگز تجربه نکرده اید قدردانی کنید. این فرآیند را از جمله با سایر جنبه‌های طبیعت (مانند آسمان، ستاره‌ها، گیاهان، پرندگان، رودخانه‌ها، دریا، حیوان مورد علاقه‌تان) تکرار کنید تا زمانی که احساس کنید به طبیعت دلبستگی پیدا کرده‌اید که به تنظیم احساسات شما کمک می‌کند. دستیابی به این امر به شما کمک می کند که پس از پایان این دوره زمان بیشتری را در طبیعت بگذرانید."],
            [
                "با چشمان بسته، عکس یا آواتار ناراضی را تصور کنید و احساسات منفی خود را به عکس یا آواتار ناخوشایند نشان دهید.",
                "در حین انجام این کار:",
                "(۱) با صدای بلند به کودک اطمینان دهید.",
                "(۲) صورت، گردن یا سر خود را ماساژ دهید.",
                "این مراحل را تا زمانی که آرام شوید تکرار کنید.",
            ],
            [
                "با چشمان بسته، یک قسمت دردناک دوران کودکی، مانند آزار عاطفی یا فیزیکی یا از دست دادن یک چهره مهم را با تمام جزئیاتی که هنوز به خاطر دارید، به یاد بیاورید. چهره کودکی که در گذشته بودید را با عکس یا آواتار ناراحت انتخاب شده مرتبط کنید. همانطور که احساسات مرتبط مانند درماندگی، تحقیر و خشم را با چشمان بسته به یاد می آورید، خود فعلی‌تان را تصور کنید که مانند یک پدر یا مادر خوب در صحنه دخالت می کند.",
                "بزرگسالی خود را تصویر کنید:",
                   "(۱) مثل هر پدر و مادر خوبی که فرزندش در مضیقه است به سرعت به فرزند خود نزدیک شوید.",
                   "(۲) با صدای بلند به کودک اطمینان می دهید که اکنون برای نجات او آمده اید، با ایستادن با صدای بلند در مقابل هر عاملی، به عنوان مثال: «چرا فرزندم را می زنی؟» و برای مثال با حمایت از کودک با صدای بلند: «عزیزم، من دیگر نمی گذارم آنها به تو آسیب برسانند».",
                   "(۳) با خود ماساژ دادن صورت، گردن یا سر، کودکتان را با تخیل در آغوش بگیرید.",
                "(۱)، (۲)، (۳) را تا زمانی که آرامش و تسکین پیدا کنید، تکرار کنید و بر ضربه تسلط پیدا کنید.",
            ],
            ["برای این تمرین، سعی کنید مانند یک کودک رفتار کنید: عضلات صورت و بدن را شل کنید، دهان خود را باز کنید و آهنگ مورد علاقه خود را در حالی که می خندید (یا حداقل لبخند می زنید) بخوانید."],
            ["بلافاصله پس از انجام کاری، به عنوان مثال، انجام کارهای خانه، گفتگو با همسایه یا خواندن یک مقاله، و با تصور اینکه این یک دستاورد است لبخند بزنید، سپس وقتی بهتر شدید، حداقل برای ده ثانیه شروع به خندیدن کنید."],
            ["با نگاه کردن به عکس یا آواتار شاد خود، لبخند بزنید و سپس برای حداقل ده ثانیه شروع به خندیدن کنید. این روند را حداقل سه بار تکرار کنید."],
            ["زمانی که تنها هستید، دهان خود را کمی باز کنید، ماهیچه های صورت خود را شل کنید، ابروهای خود را بالا بیاورید، سپس به آرامی و به طور مداوم یکی از صداهای زیر را تکرار کنید که هر کدام از آنها حداقل انرژی را مصرف می کند: «ها، هه، ها، هه» یا «ها، ها، ها، ها»; یا «هو، هو، هو، هو»؛ یا «هی، هی، هی، هی» یا «یا، یا، یا، یا». اگر به موضوعی برای خندیدن نیاز دارید، می توانید به حماقت این تمرین بخندید! هنگامی که این خنده عمدی مداوم به یک عادت تبدیل می شود، می توانید آن را مطابق با شخصیت و سبک خود شکل دهید تا سبک خنده‌ی خاص خودتان را ایجاد کنید."],
            ["به گلدان سیاه خیره شوید. لحظه ای که درک شما تغییر می کند و دو چهره سفید را می بینید که بزرگسال و کودک هستند و به یکدیگر نگاه می کنند (IT، ST، PT) بخندید یا حداقل برای یک دقیقه لبخند بزنید. به دو صورت سفید خیره شوید و لحظه‌ای که درک شما تغییر کرد و گلدان سیاه (IT, ST) را دیدید، بخندید یا حداقل یک دقیقه لبخند بزنید."],
            ["رویداد دردناکی را که در گذشته رخ داده است تجسم کنید (ممکن است یک رویداد اخیر باشد که با آن دست و پنجه نرم کرده اید یا یک رویداد دردناک که در دوران کودکی شما رخ داده و مدت زیادی تحمل کرده اید) و با وجود دردناک بودن آن، سعی کنید تاثیر مثبتی که برای شما داشته است را ببینید. از هر یک از روش‌ها برای طنز استفاده کنید تا در آن رویداد بخندید یا حداقل لبخند بزنید."],
            ["سعی کنید هر گونه الگویی از احساسات خودشیفته و ضد اجتماعی را که فرزندتان در روابط فعلی یا گذشته شما انجام داده است یا هر گونه کینه طولانی مدتی که علیه کسی ایجاد شده است، شناسایی کنید. سپس تلاش کنید تشخیص دهید که چه مقدار از زمان و انرژی شما صرف این گونه رفتارها و رنجش می شود."],
            [
                "روش جدیدی را برای مدیریت در آینده با آنچه که به عنوان احساسات ضد اجتماعی یا نارضایتی شخصی در زندگی خود شناسایی کرده اید، ایجاد کنید.",
                "۱- بدون انکار این احساسات، سعی کنید آنها را بازتاب دهید و در خود نگه دارید و از اعمال آنها بپرهیزید. سعی کنید کینه شخصی را کنار بگذارید. این ممکن است سخت و چالش برانگیز باشد اما برای رشد عاطفی ضروری است. در اینجا، شما موضعی انتقادی اما سازنده نسبت به فرزند خود می گیرید و شفقت آینده نگری را اعمال می کنید.",
                "۲- راهی مثبت برای هدایت مجدد انرژی پرخاشگرانه ناشی از این احساسات به کار مولد (مثلاً رفتن برای ورزش کردن، صحبت با یک دوست و غیره) و در نهایت به کار خلاقانه در جهت هدف والای خود در زندگی پیدا کنید.",
            ],
            ["در زندگی گذشته خود به دنبال شخصیتی دلسوز باشید که با مهربانی و کمک به برخی کلمات حکیمانه در هنگام بروز مشکل، شما را تحت تاثیر قرار داده است.",
                "به عنوان مثال، یکی از اقوام یا دوستان بزرگتر، آشنای خانوادگی، معلم، مشاور یا درمانگر که ممکن است فوت کرده باشد یا ممکن است قابل تماس نباشد.",
                "به یاد بیاورید که چه احساساتی را در زمان دریافت مهربانی و شفقت از این چهره گذرانده اید و چقدر این برای شما احساسی بود.",
                "توجه خود را متمرکز کنید و این شخصیت را به عنوان الگوی ایده آل خود انتخاب کنید.",
                "با خواندن آهنگ عاشقانه مورد علاقه خود با صدای بلند در هنگام یادآوری تمام خاطرات گرامی خود از آنها، با این شخصیت پیوند عاشقانه افلاطونی ایجاد کنید.",
                "یک آهنگ خاص که ممکن است امتحان کنید این است «من نمی توانم از عاشق شدن با تو جلوگیری کنم»."],
            ["چارچوب ایدئولوژیک معمول خود را به چالش بکشید تا هر گونه الگوی اعتقادی یک طرفه را تضعیف کنید و خودانگیختگی و بررسی هر موضوعی را از منظرهای چندگانه تشویق کنید. این را با موضوعات یا مضامینی که اعتقادات عمیقی در مورد آنها دارید و همچنین به آنها علاقه مند هستید، تمرین کنید. این ممکن است شامل هر گونه اجتماعی باشد. ، مسائل سیاسی یا اخلاقی مانند ازدواج، گرایش جنسی یا نژادپرستی. برای مثال، دیدگاه سیاسی شما در مورد یک موضوع خاص هر چه باشد، موضوع را از دیدگاه لیبرال و محافظه کار و یا از دیدگاه جناح چپ و راست در نظر بگیرید. سعی کنید هر دو طرف موضوع را درک کنید و چارچوب ایدئولوژیک غالب خود را به چالش بکشید، این بدان معنا نیست که دیدگاه خود را تغییر می دهید، بلکه به شما امکان می دهد موضوع را از منظرهای مختلف ببینید و بتوانید خود را به جای دیگران قرار دهید. سؤال یا موضوعی را در نظر بگیرید که با آنچه ممکن است در گذشته در حین انجام این تمرین به آن فکر می کردید متفاوت باشد و حداقل ۵ دقیقه این کار را انجام دهید."],
            ["فهرستی از جملات تاکیدی الهام‌بخش توسط چهره‌هایی که تحسین می‌کنید جمع آوری کنید. سه موردی را انتخاب کنید که بیشتر به شما الهام می بخشد. آنها را بخوانید و به آرامی برای حداقل سه دقیقه تکرار کنید."],
            ["- پس از یکسان سازی اولیه یک تراژدی، بدون شک با افزایش احساسات منفی، به یاد داشته باشید که نیچه برای همه افرادی که از او مراقبت می کرد آرزو می کرد رنج و ویرانی شدیدی را تحمل کنند، که بسیار خنده دار است:",
             "برای آن انسان هایی که برای من نگران هستند، آرزوی رنج، ویرانی، بیماری، بدرفتاری، خواری و خواری دارم – آرزو می کنم که آنها با تحقیر عمیق خود، شکنجه بی اعتمادی به خود، بدبختی ناآشنا نمانند. از مغلوب‌ها: من برای آنها ترحم نمی‌کنم، زیرا برایشان آرزو می‌کنم تنها چیزی که امروز می‌تواند ثابت کند که آیا کسی ارزشی دارد یا نه، این است که تحمل کند.»",
             "- پس با فکر کردن به مصیبت خود، این نقل قول را با صدای بلند بخوانید و به محض اینکه به این جمله رسیدید:",
             "«آرزو می کنم رنج، ویرانی، بیماری، بدرفتاری، ...»، شروع به خندیدن کنید و با خواندن کل نقل قول به خندیدن ادامه دهید.",
             "فقط می‌خواهم اضافه کنم که خوب است این تمرین را امتحان کنید و اکنون که روحیه مثبتی دارید با آن آشنا شوید، اما همچنین پیشنهاد می‌کنم هر زمان که احساسات منفی را تجربه کردید، آن را امتحان کنید."
             ],
            [
                "- ما ناخودآگاه از مدل کار درونی خود استفاده می کنیم که از محیط اولیه خود آموخته ایم تا دنیای اجتماعی را برای انجام عمل تفسیر کنیم.",
                "- از بسیاری جهات، ما ممکن است به طور ناخودآگاه از روشی که مراقبان اولیه ما تعاملات اجتماعی را برای انجام اقدام تفسیر کردند، تقلید کنیم.",
                "- شروع به تعدیل در این تفاسیر کنید تا الگوی رفتاری انتخاب شده بهینه تری ایجاد کنید که با رشد عاطفی شما مطابقت دارد.",
                "بهتر است اکنون که روحیه مثبتی دارید به این تمرین فکر کنید و حتی آن را امتحان کنید، اما من قویاً توصیه می کنم هر زمان که احساسات منفی را تجربه کردید، آن را نیز انجام دهید."
            ],
            [
                "بزرگسال از جنبه های مثلث تروما آگاه می شود: آزار دهنده داخلی، قربانی و نجات دهنده.",
                "بزرگسال تأثیرات این مثلث (خودشیفتگی و عدم خلاقیت) را در زندگی روزمره و تجربیات قبلی بررسی می کند.",
                "بزرگسالان تجربیات مهم زندگی و دیدگاه های اجتماعی و سیاسی خود را در بزرگسالی با آگاهی از نحوه عملکرد آزاردهنده داخلی مرور می کند.",
                "بزرگسالان فهرستی از نمونه ها را از تجربیات خود برای چهار روش مختلف که آزاردهنده داخلی عمل می کند ایجاد می کند.",
                "بزرگسالان تجربیات زندگی خود را به دقت تجزیه و تحلیل می کند تا نمونه هایی از آسیب دیدن، آسیب دیدگی توسط آزاردهنده داخلی و فرافکنی آزاردهنده درونی به دیگران باشد.",
                "بر اساس موارد فوق، بزرگسالان دوباره تجربیات خود را ارزیابی می کنند، شامل آزار و اذیت درونی، ذهنیت قربانی و بازی های سرزنش می شوند که امکان توسعه خلاقیت را فراهم می کند.",
            ],
            [
                "بعد از اینکه سطح ناراحتی کودک کاهش یافت و همچنان که به تمرین برای تعدیل عواطف منفی و تمرینات خنده ادامه دادیم، از کودک خود موارد زیر را می خواهیم:",
                "- چگونه میتونی بحران را راهی برای قوی تر شدن ببینی؟ (ها ها ها).",
                "- چگونه میتونی بحران را راهی برای رسیدن به هدف والای خود تعبیر کنی؟ (ها ها ها).",
                "- آیا احساسات آزاردهنده داخلی دوباره به دیگران فرافکنی کرده اند؟",
                "بزرگسال سوالات زیر را می پرسد:",
                "- شباهت این بحران با بحران هایی که قبلاً با آن مواجه شده ام چیست؟",
                "- چقدر شبیه بحران خانوادگی است که در کودکی تجربه کردم؟",
                "- آیا ویژگی های مثبت طرف مقابل بیشتر از ویژگی های منفی او نیست؟",
                "- یک فرد بالغ چگونه بحران را در مقایسه با فرزند من تفسیر می کند؟",
                "- آیا می توانم آن را از منظر دیگری ببینم؟",
                "- آیا می توانم خودم را جای آنها بگذارم و تأثیرات آنها را درک کنم؟",
                "- با توجه به بینش جدیدم، آیا می توانم راهی برای آرام کردن افراد درگیر در بحران پیدا کنم تا بتوانیم راه حل بهتری برای آن پیدا کنیم؟",
                "- اگر نمی توانم، آیا می توانم با احترام فاصله خود را حفظ کنم و به مشاجره یا درگیری پایان دهم؟",
            ],
            [
                "بزرگسال ما از فرزندمان می پرسد که آیا منطقی است که مطیع سیستم سودآوری فوق العاده‌ای باشیم که ما را به شرایط کنونی رسانده است؟",
                "آیا من واقعاً به همه این محصولات، اشیا و خدمات مورد نظر به دنبال پیام‌های بی‌شمار و فشارهای همسالان یا فشارهای اجتماعی بر من نیاز دارم؟",
                "آیا زمانی که زندگی در خطر نابودی نزدیکی هست، میل به یک سبک زندگی مادی‌گرا یا لذت‌پرستانه و خودخواهانه منطقی است؟",
                "آیا می‌خواهیم به این بازی مادی‌گرایانه صفر ادامه دهیم یا می‌خواهیم اهداف والای خود را در رسیدگی به مشکلات وجودی خود دنبال کنیم؟",
                "آیا ما می‌توانیم سیاره زنده را نجات دهیم جز با کار در جهت یک قرارداد اجتماعی جدید جهانی مبتنی بر همبستگی جهانی که در آن می‌توان تهاجم انسانی را به خلاقیت برای خیر عمومی تبدیل کرد؟",
            ],
        ]


def sentiment_analysis(message):
    for h in happiness:
        if h in message:
            for v in negative_verbs:
                if v in message:
                    return "SAD"
            return "HAPPY"
    for s in sadness:
        if s in message:
            for v in negative_verbs:
                if v in message:
                    return "HAPPY"
            return "SAD"
    return "NEUTRAL"


def yes_no_detection(message):
    for y in yes:
        if y in message:
            return "YES"
    for n in no:
        if n in message:
            return "NO"


def check_emotion_positiveness(emo):
    for p in positive_emotions:
        if emo == p:
            return "POS"
    for n in negative_emotions:
        if emo == n:
            return "NEG"


def check_event_time(message):
    for r in recent:
        if r in message:
            return "RECENT"
    for l in long_time:
        if l in message:
            return "NOT_RECENT"


def shuffle_lst(lst):
    random.shuffle(lst)
    return 0

def protocol_generator(p_num):
    res = "\n\n" + protocol_titles[p_num] + "\n\n"
    for p in protocols[p_num]:
        res += p
        res += "\n"
    return res


emotion = ""


def information_retrieval_module(state, message, suggested_protocol_pool, addtionals_lst, addtional_num):
    global emotion
    ## Greeting 
    if state == "GREETING": 
        b = shuffle_lst(additionals)
        return random.choice(greeting), "FEELING", suggested_protocol_pool, ["سلام", "درود"], additionals, b

    # Feeling 
    elif state == "FEELING": 
        return random.choice(feeling), "EMOTION_VERIFIER", suggested_protocol_pool, ["خوبم", "ناراحتم"], addtionals_lst, addtional_num

    # Ask if detected feeling is correct? 
    elif state == "EMOTION_VERIFIER":
        if sentiment_analysis(message) == "HAPPY":
            emotion = "HAPPY"
            return random.choice(emotion_verifier).replace("X", "خوشحالی"), "EMOTION_VERIFIER2", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
        elif sentiment_analysis(message) == "SAD":
            emotion = "SAD"
            return random.choice(emotion_verifier).replace("X", "ناراحتی"), "EMOTION_VERIFIER2", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
        elif sentiment_analysis(message) == "NEUTRAL":
            emotion = "NEUTRAL"
            return "به نظرم میاد که احساسات ناراحت‌کننده یا شادی نداری. اگر کمک دیگه‌ای میتونستم بهت بکنم خوشحال میشم بهم بگی.", "END", suggested_protocol_pool, ["ممنون", "متشکرم"], addtionals_lst, addtional_num
    
    # Check if emtion verified corre
    elif state == "EMOTION_VERIFIER2":
        if yes_no_detection(message) == "YES":
            if check_emotion_positiveness(emotion) == "POS":
                return random.choice(if_need_any_protocols), "IF_NEED_ANY_PROTOCOLS", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
            elif check_emotion_positiveness(emotion) == "NEG":
                return random.choice(event), "EVENT", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
            else:
                 return "به نظرم میاد که احساسات ناراحت‌کننده یا شادی نداری. اگر کمک دیگه‌ای میتونستم بهت بکنم خوشحال میشم بهم بگی.", "END", suggested_protocol_pool, ["ممنون", "متشکرم"], addtionals_lst, addtional_num
        elif yes_no_detection(message) == "NO":
            return random.choice(tell_emotion), "EMOTION_DETECTOR", suggested_protocol_pool, ["خوشحالم", "ناراحتم"], addtionals_lst, addtional_num
        else:
            return "لطفا با بله یا خیر بهم بگو.", "EMOTION_VERIFIER2", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num

    # Emtion Detector
    elif state == "EMOTION_DETECTOR":
        if sentiment_analysis(message) == "HAPPY":
            emotion = "HAPPY"
        elif sentiment_analysis(message) == "SAD":
            emotion = "SAD"
        elif sentiment_analysis(message) == "NEUTRAL":
            emotion = "NEUTRAL"
            
        if check_emotion_positiveness(emotion) == "POS":
            return random.choice(if_need_any_protocols), "IF_NEED_ANY_PROTOCOLS", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
        elif check_emotion_positiveness(emotion) == "NEG":
            suggested_protocol_pool.extend([18, 19, 8, 17, 16])
            return random.choice(event), "EVENT", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
        else:
            return "فکر می‌کنم مشکلی پیش اومده.", "FEELING", suggested_protocol_pool, ["مشکلی نیست"], addtionals_lst, addtional_num

    # Ask if user needs any protocols (in case of happiness)?
    elif state == "IF_NEED_ANY_PROTOCOLS":
        if yes_no_detection(message) == "YES":
            suggested_protocol_pool.extend([16, 22, 8, 9, 18, 19, 13, 14, 15, 27, 20, 23, 24])
            random.shuffle(suggested_protocol_pool)
            current_protocol = suggested_protocol_pool.pop(0)
            return {"response": "لطفا تمرین زیر رو انجام بده.", "title": protocol_titles[current_protocol] , "details": protocols[current_protocol]}, "PROTOCOL_SUGGESTING2", suggested_protocol_pool, ["نمیتونم انجامش بدم", "باشه"], addtionals_lst, addtional_num
        if yes_no_detection(message) == "NO":
            return "ممنون که باهام صحبت کردی :)", "END", suggested_protocol_pool, ["خدانگهدار", "روز بخیر"], addtionals_lst, addtional_num

    # Event
    elif state == "EVENT":
        if yes_no_detection(message) == "YES":
            return random.choice(time), "EVENT_TIME", suggested_protocol_pool, ["خیلی وقت پیش بوده", "اخیرا اتفاق افتاده"], addtionals_lst, addtional_num
        if yes_no_detection(message) == "NO":
            suggested_protocol_pool.extend([10])
            return "میتونم بازم سوال بپرسم؟", "ADDITIONAL", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num

    # Ask if event was recent?
    elif state == "EVENT_TIME":
        if check_event_time(message) == "RECENT":
            suggested_protocol_pool.extend([10])
            return "میتونم ازت بازم سوال بپرسم؟", "ADDITIONAL", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
        if check_event_time(message) == "NOT_RECENT":
            return "آیا تمرین ۱۰ باعث ناراحتی شما می‌شود؟" + protocol_generator(11), "PROTOCOL_10", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num

    # Ask if protocol 10 is distressing?
    elif state == "PROTOCOL_10":
        if yes_no_detection(message) == "YES":
            suggested_protocol_pool.extend([16])
            return "میتونم بازم سوال بپرسم؟", "ADDITIONAL", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
        if yes_no_detection(message) == "NO":
            suggested_protocol_pool.extend([11])
            return "میتونم بازم سوال بپرسم؟", "ADDITIONAL", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num


    # Additional Questions
    elif state == "ADDITIONAL":
        if yes_no_detection(message) == "YES":
            return random.choice(addtionals_lst[addtional_num]["questions"]), "ADDITIONAL_RESPONSE", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num+1
        if yes_no_detection(message) == "NO":
            if len(suggested_protocol_pool) > 0:
                random.shuffle(suggested_protocol_pool)
                current_protocol = suggested_protocol_pool.pop(0)
                return {"response": "لطفا تمرین زیر رو انجام بده.", "title": protocol_titles[current_protocol] , "details": protocols[current_protocol]}, "PROTOCOL_SUGGESTING2", suggested_protocol_pool, ["نمیتونم انجامش بدم", "باشه"], addtionals_lst, addtional_num
            else:
                return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num

    # Additional Questions
    elif state == "ADDITIONAL_RESPONSE":
        if yes_no_detection(message) == "YES":
            suggested_protocol_pool.extend(addtionals_lst[addtional_num-1]["YES"])
            if addtional_num < 7:
                return "میتونم بازم سوال بپرسم؟", "ADDITIONAL", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
            else:
                if len(suggested_protocol_pool) > 0:
                    random.shuffle(suggested_protocol_pool)
                    current_protocol = suggested_protocol_pool.pop(0)
                    return {"response": "لطفا تمرین زیر رو انجام بده.", "title": protocol_titles[current_protocol] , "details": protocols[current_protocol]}, "PROTOCOL_SUGGESTING2", suggested_protocol_pool, ["نمیتونم انجامش بدم", "باشه"], addtionals_lst, addtional_num
                else:
                    return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num


        if yes_no_detection(message) == "NO":
            suggested_protocol_pool.extend(addtionals_lst[addtional_num-1]["NO"])
            if addtional_num < 7:
                return "میتونم بازم سوال بپرسم؟", "ADDITIONAL", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num
            else:
                if len(suggested_protocol_pool) > 0:
                    random.shuffle(suggested_protocol_pool)
                    current_protocol = suggested_protocol_pool.pop(0)
                    return {"response": "لطفا تمرین زیر رو انجام بده.", "title": protocol_titles[current_protocol] , "details": protocols[current_protocol]}, "PROTOCOL_SUGGESTING2", suggested_protocol_pool, ["نمیتونم انجامش بدم", "باشه"], addtionals_lst, addtional_num
                else:
                    return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num


    # Protocol Suggesting
    elif state == "PROTOCOL_SUGGESTING":
        if len(suggested_protocol_pool) > 0:
            random.shuffle(suggested_protocol_pool) 
            current_protocol = suggested_protocol_pool.pop(0)
            return {"response": "لطفا تمرین زیر رو انجام بده.", "title": protocol_titles[current_protocol] , "details": protocols[current_protocol]}, "PROTOCOL_SUGGESTING2", suggested_protocol_pool, ["نمیتونم انجامش بدم", "باشه"], addtionals_lst, addtional_num
        else:
            return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num

    elif state == "PROTOCOL_SUGGESTING2":
        if yes_no_detection(message) == "YES":
            return "لطفا انجامش بده و بعد بهم بگو که حالت بهتره؟", "PROTOCOL_SUGGESTING3", suggested_protocol_pool, ["هنوز خوب نیستم", "بهترم"], addtionals_lst, addtional_num
        if yes_no_detection(message) == "NO":
            return "آیا تمرین دیگه‌ای میخوای بهت پیشنهاد بدم؟", "PROTOCOL_SUGGESTING_AGAIN", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num

    elif state == "PROTOCOL_SUGGESTING_AGAIN":
        if yes_no_detection(message) == "YES":
            if len(suggested_protocol_pool) > 0: 
                random.shuffle(suggested_protocol_pool)
                current_protocol = suggested_protocol_pool.pop(0)
                return {"response": "لطفا تمرین زیر رو انجام بده.", "title": protocol_titles[current_protocol] , "details": protocols[current_protocol]}, "PROTOCOL_SUGGESTING2", suggested_protocol_pool, ["نمیتونم انجامش بدم", "باشه"], addtionals_lst, addtional_num
            else:
                return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num
        if yes_no_detection(message) == "NO":
            return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num
        
    # Protocol Suggesting
    elif state == "PROTOCOL_SUGGESTING3":
        return "آیا تمرین دیگه‌ای میخوای بهت پیشنهاد بدم؟", "PROTOCOL_SUGGESTING_AGAIN", suggested_protocol_pool, ["بله", "خیر"], addtionals_lst, addtional_num

    # Thank user
    elif state == "END":
        return "ممنون که باهام صحبت کردی :)", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num

    # End of Conversation
    elif state == "END2":
        return "امیدوارم تونسته باشم کمکت کنم.", "END2", suggested_protocol_pool, ["متشکرم", "ممنون"], addtionals_lst, addtional_num
    return

