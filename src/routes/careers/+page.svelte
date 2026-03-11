<script>
	import { onMount } from 'svelte';

	let heroVisible = $state(false);
	let sections = $state({});

	const departments = ['Все', 'Производство', 'Дизайн', 'Продажи', 'IT', 'Управление'];
	let activeDept = $state('Все');

	const vacancies = [
		{
			id: 1,
			title: 'Технолог мебельного производства',
			dept: 'Производство',
			city: 'Барановичи',
			type: 'Полная занятость',
			experience: 'от 3 лет',
			salary: 'от 2 500 BYN',
			description:
				'Разработка и оптимизация технологических процессов производства корпусной мебели. Контроль качества на всех этапах.',
			tags: ['Производство', 'Технология', 'Контроль качества']
		},
		{
			id: 2,
			title: 'Дизайнер интерьеров (кухни)',
			dept: 'Дизайн',
			city: 'Барановичи / Удалённо',
			type: 'Полная занятость',
			experience: 'от 2 лет',
			salary: 'от 1 800 BYN',
			description:
				'Создание дизайн-проектов кухонь по запросам клиентов. Работа с 3D-редакторами, визуализация, презентация решений.',
			tags: ['AutoCAD', '3ds Max', 'PRO100']
		},
		{
			id: 3,
			title: 'Менеджер по продажам (B2B)',
			dept: 'Продажи',
			city: 'Минск',
			type: 'Полная занятость',
			experience: 'от 2 лет',
			salary: 'от 2 000 BYN + %',
			description:
				'Развитие дилерской сети в регионах Беларуси. Ведение переговоров, заключение договоров, сопровождение партнёров.',
			tags: ['B2B', 'Переговоры', 'CRM']
		},
		{
			id: 4,
			title: 'Frontend-разработчик (SvelteKit)',
			dept: 'IT',
			city: 'Удалённо',
			type: 'Полная занятость',
			experience: 'от 2 лет',
			salary: 'от 3 500 BYN',
			description:
				'Разработка и поддержка веб-интерфейсов фабрики. Работа в современном стеке: SvelteKit, TypeScript, Tailwind CSS.',
			tags: ['SvelteKit', 'TypeScript', 'Tailwind']
		},
		{
			id: 5,
			title: 'Оператор станков с ЧПУ',
			dept: 'Производство',
			city: 'Барановичи',
			type: 'Полная занятость',
			experience: 'от 1 года',
			salary: 'от 1 600 BYN',
			description:
				'Управление оборудованием с ЧПУ на производстве МДФ-фасадов. Программирование, наладка, текущее обслуживание.',
			tags: ['ЧПУ', 'МДФ', 'Наладка']
		},
		{
			id: 6,
			title: 'Руководитель отдела продаж',
			dept: 'Управление',
			city: 'Барановичи',
			type: 'Полная занятость',
			experience: 'от 5 лет',
			salary: 'от 4 000 BYN',
			description:
				'Формирование стратегии продаж, управление командой из 12 менеджеров, выполнение плановых показателей.',
			tags: ['Управление', 'KPI', 'Стратегия']
		},
		{
			id: 7,
			title: 'UX/UI-дизайнер',
			dept: 'Дизайн',
			city: 'Удалённо',
			type: 'Полная / Частичная',
			experience: 'от 2 лет',
			salary: 'от 2 200 BYN',
			description:
				'Проектирование пользовательских интерфейсов для сайта и внутренних систем фабрики. Разработка дизайн-системы.',
			tags: ['Figma', 'UI Kit', 'Прототипирование']
		},
		{
			id: 8,
			title: 'Контент-менеджер / Копирайтер',
			dept: 'Продажи',
			city: 'Удалённо',
			type: 'Частичная занятость',
			experience: 'от 1 года',
			salary: 'от 900 BYN',
			description:
				'Создание контента для сайта, социальных сетей и рекламных материалов. Описания коллекций, статьи, новости.',
			tags: ['Копирайтинг', 'SEO', 'Соцсети']
		}
	];

	const filteredVacancies = $derived(
		activeDept === 'Все' ? vacancies : vacancies.filter((v) => v.dept === activeDept)
	);

	const perks = [
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.171-.879-1.171-2.303 0-3.182.53-.398 1.267-.62 2.003-.62.736 0 1.472.222 2.003.62M12 6V4m0 14v2"/>`,
			title: 'Конкурентная зарплата',
			text: 'Своевременная выплата, привязанная к результату. Ежегодный пересмотр.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>`,
			title: 'Официальное трудоустройство',
			text: 'Оформление по ТК, полный соцпакет, оплачиваемый отпуск.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5"/>`,
			title: 'Обучение и развитие',
			text: 'Внутренние тренинги и профессиональные экскурсии от наших партнёров.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"/>`,
			title: 'Дружная команда',
			text: 'Более 300 сотрудников. Открытая командная культура и регулярные мероприятия.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"/>`,
			title: 'Скидка на продукцию',
			text: 'Корпоративная скидка 30% на всю мебель фабрики ЗОВ для сотрудников.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3"/>`,
			title: 'Карьерный рост',
			text: 'Прозрачная система продвижения. Каждый второй руководитель вырос в компании.'
		}
	];

	let expandedId = $state(/** @type {number|null} */ (null));

	/** @type {string} */
	let resumeName = $state('');
	/** @type {string} */
	let resumePhone = $state('');
	/** @type {string} */
	let resumeEmail = $state('');
	/** @type {string} */
	let resumeMessage = $state('');
	let resumeSent = $state(false);

	function submitResume(/** @type {SubmitEvent} */ e) {
		e.preventDefault();
		resumeSent = true;
	}

	onMount(() => {
		heroVisible = true;

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						sections[entry.target.id] = true;
					}
				});
			},
			{ threshold: 0.07, rootMargin: '0px 0px -40px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => observer.observe(el));
		return () => observer.disconnect();
	});
</script>

<svelte:head>
	<title>Вакансии — ЗОВ | Работа на мебельной фабрике</title>
	<meta
		name="description"
		content="Открытые вакансии фабрики ЗОВ: производство, дизайн, IT, продажи. Официальное трудоустройство, конкурентная зарплата, профессиональное развитие."
	/>
</svelte:head>

<!-- ==================== HERO ==================== -->
<section class="relative overflow-hidden bg-primary py-28 lg:py-36">
	<!-- Decorations -->
	<div
		class="absolute top-0 left-0 h-72 w-72 -translate-x-1/2 -translate-y-1/2 rotate-12 border border-white/5"
	></div>
	<div
		class="absolute right-0 bottom-0 h-96 w-96 translate-x-1/3 translate-y-1/3 border border-white/5"
	></div>
	<div class="absolute top-10 left-1/2 h-40 w-40 -translate-x-1/2 border border-white/[0.04]"></div>

	<div
		class="absolute top-0 left-0 h-px w-full bg-gradient-to-r from-transparent via-secondary to-transparent opacity-30"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="max-w-2xl">
			<div class="opacity-0" class:animate-fade-up={heroVisible} style="animation-delay:0.2s">
				<span
					class="inline-flex items-center gap-2 border border-white/10 bg-white/5 px-4 py-2 text-[11px] tracking-[0.3em] text-accent uppercase backdrop-blur-sm"
				>
					<span class="h-1.5 w-1.5 rounded-full bg-accent"></span>
					Карьера в ЗОВ
				</span>
			</div>

			<h1
				class="mt-6 text-5xl leading-[1.1] font-light text-white opacity-0 md:text-6xl lg:text-7xl"
				style="font-family: var(--font-heading); animation-delay: 0.4s"
				class:animate-fade-up={heroVisible}
			>
				Строй карьеру<br />
				<span class="text-accent-light">вместе с нами</span>
			</h1>

			<p
				class="mt-7 max-w-lg text-base leading-relaxed text-white/60 opacity-0 md:text-lg"
				class:animate-fade-up={heroVisible}
				style="animation-delay: 0.6s"
			>
				Фабрика ЗОВ — это более 300 специалистов, которые создают премиальную мебель для тысяч
				белорусских семей. Присоединяйтесь к команде профессионалов.
			</p>

			<div
				class="mt-10 flex flex-wrap items-center gap-4 opacity-0"
				class:animate-fade-up={heroVisible}
				style="animation-delay: 0.8s"
			>
				<a
					href="#vacancies"
					class="group inline-flex items-center gap-3 border border-accent bg-accent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
				>
					Смотреть вакансии
					<svg
						class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						stroke-width="1.5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
						/>
					</svg>
				</a>
				<a
					href="#open-resume"
					class="inline-flex items-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white/80 uppercase transition-all duration-500 hover:border-white/50 hover:text-white"
				>
					Отправить резюме
				</a>
			</div>
		</div>

		<!-- Stats -->
		<div
			class="mt-20 grid grid-cols-2 gap-px border border-white/10 opacity-0 md:grid-cols-4"
			class:animate-fade-up={heroVisible}
			style="animation-delay: 1s"
		>
			{#each [{ value: '300+', label: 'сотрудников' }, { value: `${vacancies.length}`, label: 'открытых вакансий' }, { value: '25 лет', label: 'на рынке' }, { value: '30%', label: 'скидка для сотрудников' }] as stat}
				<div class="flex flex-col gap-1.5 bg-white/5 px-6 py-5 backdrop-blur-sm">
					<span
						class="text-3xl font-light text-accent-light"
						style="font-family: var(--font-heading);">{stat.value}</span
					>
					<span class="text-xs tracking-wide text-white/40">{stat.label}</span>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== PERKS ==================== -->
<section class="py-20 lg:py-28" id="perks-section" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<div
			class="mb-14 opacity-0 transition-all duration-700"
			class:animate-fade-up={sections['perks-section']}
		>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Почему ЗОВ</span>
			<h2
				class="mt-3 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Условия работы
			</h2>
		</div>

		<div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
			{#each perks as perk, i}
				<div
					class="group border border-border-light bg-white p-8 opacity-0 shadow-card transition-all duration-500 hover:-translate-y-1 hover:shadow-elevated"
					class:animate-fade-up={sections['perks-section']}
					style="animation-delay: {0.08 + i * 0.07}s"
				>
					<div
						class="mb-5 flex h-10 w-10 items-center justify-center border border-secondary/20 text-secondary transition-colors duration-300 group-hover:border-secondary group-hover:bg-secondary group-hover:text-white"
					>
						<svg
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							{@html perk.icon}
						</svg>
					</div>
					<h3
						class="text-lg font-medium text-primary transition-colors duration-300 group-hover:text-secondary"
						style="font-family: var(--font-heading);"
					>
						{perk.title}
					</h3>
					<p class="mt-3 text-sm leading-relaxed text-text-secondary">{perk.text}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== VACANCIES ==================== -->
<section class="bg-surface-warm py-20 lg:py-28" id="vacancies" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header + filter -->
		<div
			class="mb-10 flex flex-col gap-6 opacity-0 transition-all duration-700 sm:flex-row sm:items-end sm:justify-between"
			class:animate-fade-up={sections['vacancies']}
		>
			<div>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Открытые позиции</span>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Вакансии
				</h2>
			</div>
			<p class="text-sm text-text-muted">
				{filteredVacancies.length}
				{filteredVacancies.length === 1
					? 'вакансия'
					: filteredVacancies.length < 5
						? 'вакансии'
						: 'вакансий'}
			</p>
		</div>

		<!-- Department filter -->
		<div
			class="mb-8 flex flex-wrap gap-2 opacity-0 transition-all duration-700"
			class:animate-fade-up={sections['vacancies']}
			style="animation-delay: 0.15s"
		>
			{#each departments as dept}
				<button
					class="border px-4 py-2 text-xs tracking-wider uppercase transition-all duration-300
						{activeDept === dept
						? 'border-primary bg-primary text-white'
						: 'border-border-medium bg-white text-text-secondary hover:border-primary hover:text-primary'}"
					onclick={() => {
						activeDept = dept;
						expandedId = null;
					}}
					id="dept-{dept}"
				>
					{dept}
				</button>
			{/each}
		</div>

		<!-- Vacancies list -->
		<div class="divide-y divide-border-light border border-border-light bg-white">
			{#each filteredVacancies as vac, i}
				<div
					class="opacity-0 transition-all duration-500"
					class:animate-fade-up={sections['vacancies']}
					style="animation-delay: {0.25 + i * 0.06}s"
				>
					<!-- Row header (always visible) -->
					<button
						class="group w-full text-left"
						onclick={() => (expandedId = expandedId === vac.id ? null : vac.id)}
						id="vacancy-{vac.id}"
					>
						<div
							class="flex items-start gap-6 px-6 py-6 transition-colors duration-300 hover:bg-surface-warm sm:items-center sm:px-8"
						>
							<!-- Info -->
							<div class="flex flex-1 flex-col gap-1 sm:flex-row sm:items-center sm:gap-8">
								<div class="min-w-0 flex-1">
									<h3
										class="text-base font-medium text-primary transition-colors duration-300 group-hover:text-secondary"
										style="font-family: var(--font-heading);"
									>
										{vac.title}
									</h3>
									<div class="mt-1.5 flex flex-wrap items-center gap-x-3 gap-y-1">
										<span class="text-xs text-text-muted">{vac.city}</span>
										<span class="h-1 w-1 rounded-full bg-border-medium"></span>
										<span class="text-xs text-text-muted">{vac.type}</span>
										<span class="h-1 w-1 rounded-full bg-border-medium"></span>
										<span class="text-xs text-text-muted">Опыт: {vac.experience}</span>
									</div>
								</div>
								<div class="flex flex-shrink-0 flex-col items-start gap-1.5 sm:items-end">
									<span class="text-sm font-medium text-primary">{vac.salary}</span>
									<span
										class="inline-block border border-border-medium px-2.5 py-0.5 text-[10px] tracking-wider text-text-muted uppercase"
										>{vac.dept}</span
									>
								</div>
							</div>
							<!-- Arrow -->
							<svg
								class="h-5 w-5 flex-shrink-0 text-text-muted transition-all duration-300 {expandedId ===
								vac.id
									? 'rotate-180 text-secondary'
									: 'group-hover:text-secondary'}"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M19.5 8.25l-7.5 7.5-7.5-7.5"
								/>
							</svg>
						</div>
					</button>

					<!-- Expanded details -->
					{#if expandedId === vac.id}
						<div class="border-t border-border-light bg-surface-warm px-6 pt-6 pb-8 sm:px-8">
							<p class="max-w-2xl text-sm leading-relaxed text-text-secondary">{vac.description}</p>

							<div class="mt-5 flex flex-wrap gap-2">
								{#each vac.tags as tag}
									<span
										class="border border-border-medium bg-white px-3 py-1 text-[11px] tracking-wider text-text-muted uppercase"
										>{tag}</span
									>
								{/each}
							</div>

							<div class="mt-6 flex flex-wrap items-center gap-4">
								<a
									href="#open-resume"
									class="group inline-flex items-center gap-3 border border-primary bg-primary px-6 py-3 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
								>
									Откликнуться
									<svg
										class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
										stroke-width="1.5"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
										/>
									</svg>
								</a>
								<span class="text-xs text-text-muted"
									>или отправьте резюме на <a
										href="mailto:hr@zov.by"
										class="text-secondary underline underline-offset-2">hr@zov.by</a
									></span
								>
							</div>
						</div>
					{/if}
				</div>
			{/each}

			{#if filteredVacancies.length === 0}
				<div class="px-8 py-16 text-center text-text-muted">
					<p class="text-sm">Вакансий в этой категории не найдено.</p>
				</div>
			{/if}
		</div>
	</div>
</section>

<!-- ==================== OPEN RESUME ==================== -->
<section class="relative overflow-hidden bg-primary py-20 lg:py-28" id="open-resume" data-animate>
	<div
		class="absolute top-0 left-0 h-64 w-64 -translate-x-1/2 -translate-y-1/2 border border-white/5"
	></div>
	<div
		class="absolute right-0 bottom-0 h-80 w-80 translate-x-1/3 translate-y-1/3 border border-white/5"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="grid gap-16 lg:grid-cols-2 lg:gap-24">
			<!-- Left -->
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['open-resume']}
			>
				<span class="text-[11px] tracking-[0.3em] text-accent uppercase">Открытое резюме</span>
				<h2
					class="mt-4 text-4xl font-light text-white lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Не нашли<br />
					<span class="text-accent-light">подходящую вакансию?</span>
				</h2>
				<p class="mt-6 text-base leading-relaxed text-white/55">
					Отправьте открытое резюме — мы сохраняем его в базе и свяжемся, когда появится позиция,
					которая подойдёт именно вам.
				</p>

				<div class="mt-10 space-y-4">
					<div class="flex items-center gap-3">
						<div class="flex h-9 w-9 shrink-0 items-center justify-center border border-white/10">
							<svg
								class="h-4 w-4 text-accent"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"
								/>
							</svg>
						</div>
						<span class="text-sm text-white/60">hr@zov.by</span>
					</div>
					<div class="flex items-center gap-3">
						<div class="flex h-9 w-9 shrink-0 items-center justify-center border border-white/10">
							<svg
								class="h-4 w-4 text-accent"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"
								/>
							</svg>
						</div>
						<span class="text-sm text-white/60">+375 (29) 123-45-67 (HR-отдел)</span>
					</div>
				</div>
			</div>

			<!-- Right: form -->
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['open-resume']}
				style="animation-delay: 0.2s"
			>
				{#if resumeSent}
					<div class="flex h-full flex-col items-center justify-center py-12 text-center">
						<div
							class="flex h-16 w-16 items-center justify-center border border-accent/30 bg-accent/10"
						>
							<svg
								class="h-8 w-8 text-accent"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
							</svg>
						</div>
						<h3
							class="mt-6 text-2xl font-light text-white"
							style="font-family: var(--font-heading);"
						>
							Резюме отправлено
						</h3>
						<p class="mt-3 max-w-xs text-sm text-white/50">
							Мы рассмотрим вашу кандидатуру и свяжемся при появлении подходящей вакансии.
						</p>
					</div>
				{:else}
					<form
						onsubmit={submitResume}
						class="border border-white/10 bg-white/5 p-8 backdrop-blur-sm lg:p-10"
					>
						<h3
							class="mb-8 text-xl font-light text-white"
							style="font-family: var(--font-heading);"
						>
							Открытое резюме
						</h3>

						<div class="mb-5">
							<label
								for="resume-name"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
								>Имя и фамилия*</label
							>
							<input
								id="resume-name"
								type="text"
								bind:value={resumeName}
								required
								placeholder="Иван Петров"
								class="w-full border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							/>
						</div>

						<div class="mb-5">
							<label
								for="resume-phone"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
								>Телефон*</label
							>
							<input
								id="resume-phone"
								type="tel"
								bind:value={resumePhone}
								required
								placeholder="+375 (29) 000-00-00"
								class="w-full border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							/>
						</div>

						<div class="mb-5">
							<label
								for="resume-email"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
								>Email*</label
							>
							<input
								id="resume-email"
								type="email"
								bind:value={resumeEmail}
								required
								placeholder="your@email.com"
								class="w-full border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							/>
						</div>

						<div class="mb-8">
							<label
								for="resume-msg"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
								>О себе / желаемая должность</label
							>
							<textarea
								id="resume-msg"
								bind:value={resumeMessage}
								rows="3"
								placeholder="Расскажите коротко о себе и опыте..."
								class="w-full resize-none border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							></textarea>
						</div>

						<button
							type="submit"
							class="group flex w-full items-center justify-center gap-3 border border-accent bg-accent py-4 text-xs tracking-[0.2em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
						>
							Отправить резюме
							<svg
								class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
								/>
							</svg>
						</button>

						<p class="mt-4 text-center text-[11px] text-white/25">
							Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности
						</p>
					</form>
				{/if}
			</div>
		</div>
	</div>
</section>
