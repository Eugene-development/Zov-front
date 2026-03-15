<script>
	import { onMount } from 'svelte';

	let contentVisible = $state(false);

	onMount(() => {
		contentVisible = true;
	});
</script>

<svelte:head>
	<title>Пользовательское соглашение — ЗОВ</title>
	<meta
		name="description"
		content="Пользовательское соглашение компании ЗОВ. Условия использования нашего сайта, права и обязанности сторон."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[40vh] bg-surface pt-32 pb-16 lg:pt-40 lg:pb-24">
	<div class="mx-auto max-w-4xl px-6">
		<div class="opacity-0 transition-all duration-700" class:animate-fade-up={contentVisible}>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Документы</span>
			<h1
				class="mt-4 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Пользовательское <br class="md:hidden" /><span class="text-secondary">соглашение</span>
			</h1>
			<p class="mt-6 text-sm text-muted">Последнее обновление: 15 марта 2026</p>
		</div>
	</div>
</section>

<!-- ==================== CONTENT SECTION ==================== -->
<section class="relative bg-white py-16 lg:py-24">
	<div class="mx-auto max-w-4xl px-6">
		<div
			class="space-y-8 opacity-0 transition-all delay-300 duration-700"
			class:animate-fade-up={contentVisible}
		>
			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					1. Общие положения
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					1.1. Настоящее Пользовательское соглашение (далее — Соглашение) относится к сайту компании
					(далее — Сайт). Настоящее Соглашение регулирует отношения между Администрацией сайта и
					Пользователем данного Сайта.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					1.2. Использование Сайта означает согласие Пользователя с настоящим Соглашением и
					условиями использования сервисов, предоставляемых на сайте. В случае несогласия с
					условиями Пользовательского соглашения, Пользователь должен немедленно прекратить
					использование Сайта.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					1.3. Администрация сайта оставляет за собой право в любое время изменять, добавлять или
					удалять пункты настоящего Соглашения без предварительного уведомления Пользователя.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					2. Предмет соглашения
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					2.1. Предметом настоящего Соглашения является предоставление Пользователю доступа к
					информации о товарах (мебели, кухнях и сопутствующих товарах), услугах, специальных
					предложениях и сервисах (запись на дизайн-проект, подбор мебели), представленных на Сайте.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					2.2. Сайт предоставляет Пользователю следующие виды сервисов (услуг): доступ к
					электронному каталогу, предоставление контактной информации, доступ к средствам поиска и
					навигации, предоставление возможности заказа обратной связи и иных форм взаимодействия.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					3. Права и обязанности сторон
				</h2>
				<h3 class="mt-2 text-lg font-medium text-primary">3.1. Администрация сайта вправе:</h3>
				<ul
					class="list-disc space-y-2 pl-5 text-base leading-relaxed text-secondary marker:text-secondary"
				>
					<li>Изменять правила пользования Сайтом, а также изменять содержание данного Сайта.</li>
					<li>Ограничить доступ к Сайту в случае нарушения Пользователем условий Соглашения.</li>
					<li>
						Собирать и анализировать информацию о предпочтениях Пользователя для улучшения качества
						обслуживания.
					</li>
				</ul>

				<h3 class="mt-4 text-lg font-medium text-primary">3.2. Пользователь обязан:</h3>
				<ul
					class="list-disc space-y-2 pl-5 text-base leading-relaxed text-secondary marker:text-secondary"
				>
					<li>
						Предоставлять по запросу Администрации сайта дополнительную информацию, которая имеет
						непосредственное отношение к предоставляемым сервисам.
					</li>
					<li>
						Не предпринимать действий, которые могут рассматриваться как нарушающие нормальную
						работу Сайта.
					</li>
					<li>
						Соблюдать имущественные и неимущественные права авторов и иных правообладателей при
						использовании Сайта.
					</li>
					<li>Не использовать сервисы Сайта с целью совершения уголовно наказуемых деяний.</li>
				</ul>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					4. Использование материалов сайта
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					4.1. Все объекты, доступные при помощи сервисов Сайта, в том числе элементы дизайна,
					текст, графические изображения, иллюстрации, видео, являются объектами исключительных
					прав.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					4.2. Использование материалов, размещенных на сайте, допускается только с предварительного
					письменного согласия правообладателя (представителей компании).
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					5. Ответственность
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					5.1. Администрация не несет ответственности за любые прямые или косвенные убытки,
					возникшие в результате использования или невозможности использования данного Сайта.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					5.2. Информация о товарах, материалах и ценах, представленная на сайте, носит
					ознакомительный (информационный) характер и ни при каких условиях не является публичной
					офертой. Для получения подробной информации о характеристиках, наличии и стоимости товаров
					пожалуйста обращайтесь к менеджерам нашей компании.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					6. Нарушение условий соглашения
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					6.1. Администрация сайта вправе раскрыть любую информацию о Пользователе, которую
					посчитает необходимой для выполнения положений действующего законодательства.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					6.2. Администрация сайта имеет право прекратить и/или заблокировать доступ к Сайту, если
					Пользователь нарушил настоящее Соглашение или другие условия пользования Сайтом.
				</p>
			</div>

			<div class="space-y-4">
				<h2 class="text-2xl font-medium text-primary" style="font-family: var(--font-heading);">
					7. Прочие условия
				</h2>
				<p class="text-base leading-relaxed text-secondary">
					7.1. Администрация сайта не принимает встречные предложения от Пользователя относительно
					изменений настоящего Пользовательского соглашения.
				</p>
				<p class="text-base leading-relaxed text-secondary">
					7.2. Отзывы Пользователя, размещенные на Сайте, не являются конфиденциальной информацией и
					могут быть использованы Администрацией сайта без ограничений.
				</p>
			</div>
		</div>
	</div>
</section>
