run:
	@echo "Running products spider"
	scrapy crawl products -a spiders_dir=wood_wam.spiders

json:
	@echo "Running products spider to make json file"
	scrapy crawl products -O products.json -a spiders_dir=wood_wam.spiders

format:
	@echo "Run format checks"
	flake8 .
	isort .