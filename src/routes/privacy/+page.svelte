<script>
	import { onMount } from 'svelte';

	let contentVisible = $state(false);

	onMount(() => {
		contentVisible = true;
	});
</script>

<svelte:head>
	<title>Политика конфиденциальности — ЗОВ</title>
	<meta
		name="description"
		content="Политика конфиденциальности компании ЗОВ. Узнайте, как мы обрабатываем и защищаем ваши персональные данные."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[40vh] bg-surface pt-32 pb-16 lg:pt-40 lg:pb-24">
	<div class="mx-auto max-w-4xl px-6 xl:px-1">
		<div class="opacity-0 transition-all duration-700" class:animate-fade-up={contentVisible}>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Документы</span>
			<h1
				class="mt-4 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Политика <br class="md:hidden" /><span class="text-secondary">конфиденциальности</span>
			</h1>
			<p class="mt-6 text-sm text-muted">Последнее обновление: 15 марта 2026</p>
		</div>
	</div>
</section>

<!-- ==================== CONTENT SECTION ==================== -->
<section class="relative bg-white py-16 lg:py-24">
	<div class="mx-auto max-w-4xl px-6 xl:px-1">
		<div
			class="space-y-8 opacity-0 transition-all delay-300 duration-700"
			class:animate-fade-up={contentVisible}
		>
			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					1. Общие положения
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					1.1. Настоящая Политика конфиденциальности определяет порядок обработки персональных
					данных и меры по обеспечению безопасности персональных данных, предпринимаемые нашей
					компанией (далее — Оператор).
				</p>
				<p class="text-base leading-relaxed text-secondary">
					1.2. Оператор ставит своей важнейшей целью и условием осуществления своей деятельности
					соблюдение прав и свобод человека и гражданина при обработке его персональных данных, в
					том числе защиты прав на неприкосновенность частной жизни, личную и семейную тайну.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					1.3. Настоящая политика Оператора в отношении обработки персональных данных (далее —
					Политика) применяется ко всей информации, которую Оператор может получить о посетителях
					данного веб-сайта.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					2. Основные понятия, используемые в Политике
				</h2>
				<ul
					class="list-disc space-y-2 pl-5 text-base leading-relaxed text-secondary marker:text-secondary"
				>
					<li>
						<strong>Сайт</strong> — совокупность графических и информационных материалов, а также программ
						для ЭВМ и баз данных, обеспечивающих их доступность в сети интернет.
					</li>
					<li><strong>Пользователь</strong> — любой посетитель веб-сайта.</li>
					<li>
						<strong>Персональные данные</strong> — любая информация, относящаяся прямо или косвенно к
						определенному или определяемому Пользователю веб-сайта.
					</li>
					<li>
						<strong>Обработка персональных данных</strong> — любое действие (операция) или совокупность
						действий (операций), совершаемых с использованием средств автоматизации или без использования
						таких средств с персональными данными.
					</li>
				</ul>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					3. Сбор и использование персональных данных
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					Оператор может обрабатывать следующие персональные данные Пользователя:
				</p>
				<ul
					class="list-disc space-y-2 pl-5 text-base leading-relaxed text-secondary marker:text-secondary"
				>
					<li>Фамилия, Имя, Отчество;</li>
					<li>Электронный адрес (e-mail);</li>
					<li>Номера телефонов;</li>
					<li>Город проживания или местонахождения;</li>
					<li>
						Обезличенные данные о посетителях (в т.ч. файлы «cookie») с помощью сервисов
						интернет-статистики (Яндекс Метрика, Google Analytics и других).
					</li>
				</ul>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					4. Цели обработки персональных данных
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					4.1. Цель обработки персональных данных Пользователя:
				</p>
				<ul
					class="list-disc space-y-2 pl-5 text-base leading-relaxed text-secondary marker:text-secondary"
				>
					<li>информирование Пользователя посредством отправки электронных писем и звонков;</li>
					<li>заключение, исполнение и прекращение гражданско-правовых договоров;</li>
					<li>
						предоставление доступа Пользователю к сервисам, информации и/или материалам,
						содержащимся на веб-сайте;
					</li>
					<li>оказание консультационных услуг и помощь в подборе мебели;</li>
					<li>запись на бесплатный дизайн-проект.</li>
				</ul>
				<p class="text-base leading-relaxed text-secondary">
					4.2. Также Оператор имеет право направлять Пользователю уведомления о новых продуктах и
					услугах, специальных предложениях и различных событиях. Пользователь всегда может
					отказаться от получения информационных сообщений.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					5. Безопасность персональных данных
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					Безопасность персональных данных, которые обрабатываются Оператором, обеспечивается путем
					реализации правовых, организационных и технических мер, необходимых для выполнения в
					полном объеме требований действующего законодательства в области защиты персональных
					данных.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					Оператор обеспечивает сохранность персональных данных и принимает все возможные меры,
					исключающие доступ к персональным данным неуполномоченных лиц.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					6. Права пользователей
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					Пользователь может в любой момент отозвать свое согласие на обработку персональных данных,
					направив Оператору уведомление посредством электронной почты на электронный адрес
					Оператора, указанный на сайте, с пометкой «Отзыв согласия на обработку персональных
					данных».
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					7. Заключительные положения
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					7.1. Пользователь может получить любые разъяснения по интересующим вопросам, касающимся
					обработки его персональных данных, обратившись к Оператору с помощью формы обратной связи
					на сайте или по контактному телефону.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					7.2. В данном документе будут отражены любые изменения политики обработки персональных
					данных Оператором. Политика действует бессрочно до замены ее новой версией.
				</p>
			</div>
		</div>
	</div>
</section>
