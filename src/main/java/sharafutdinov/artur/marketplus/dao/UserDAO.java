package sharafutdinov.artur.marketplus.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.orm.hibernate4.HibernateTemplate;
import org.springframework.stereotype.Service;
import sharafutdinov.artur.marketplus.model.User;

import java.io.Serializable;
import java.util.List;

/**
 * Created by first on 21.03.17.
 */
@Service
public class UserDAO implements GenericDao<User,String> {

    @Autowired
    private HibernateTemplate hibernateTemplate;

    @Override
    public User load(final String id) {
        return hibernateTemplate.load(User.class,id);
    }

    @Override
    public User get(final String id) {
        return hibernateTemplate.get(User.class,id);
    }

    @Override
    public List<User> getAll() {
        return hibernateTemplate.loadAll(User.class);
    }

    @Override
    public Serializable save(final User object) {
        return hibernateTemplate.save(object);
    }

    @Override
    public void saveOrUpdate(final User object) {
        hibernateTemplate.saveOrUpdate(object);
    }

    @Override
    public void delete(final User object) {
        hibernateTemplate.delete(object);
    }

    @Override
    public Long count() {
        return new Long(hibernateTemplate.loadAll(User.class).size());
    }

    @Override
    public void flush() {
        hibernateTemplate.flush();
    }

}
