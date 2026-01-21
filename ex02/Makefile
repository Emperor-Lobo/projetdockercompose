all:
	docker compose up --build

clean:
	docker compose down

fclean:
	docker compose down --rmi all

purge:
	rm -f data/users.db

re: fclean all

.PHONY: all clean fclean purge re
